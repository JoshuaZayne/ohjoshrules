#!/usr/bin/env python3
"""
Cross-device Claude Code memory sync.

Structure in this repo:
    memory/
        shared/      -- memories that apply to every device
        desktop/     -- only loaded when running on the Windows desktop
        laptop/      -- only loaded when running on the Windows laptop / F: drive
        raspie/      -- only loaded when running on the Raspberry Pi

Usage:
    python sync_memory.py              # pull from github, merge into local Claude memory
    python sync_memory.py --pull       # same as default
    python sync_memory.py --push       # copy NEW local memory files back into this repo
    python sync_memory.py --sync       # pull first, then push, then commit+push to github
    python sync_memory.py --status     # show which device is detected and where things live
    python sync_memory.py --dry-run    # print actions without doing them

How device detection works:
    Loops through candidate paths (same pattern as device_paths.py in the
    other repos) and picks the first that exists. That determines which
    device-specific subfolder gets merged on top of `shared/`.

How "learning" works:
    When Claude saves a new memory during a session on one device, run
    `sync_memory.py --push --sync` to upload it. Other devices run
    `sync_memory.py` (pull) and pick it up. Device-specific memories
    only apply on the device they were saved from.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Device detection (loop-based, same pattern as device_paths.py)
# ---------------------------------------------------------------------------

def find_existing_path(candidates):
    """Return the first candidate that exists, else the first candidate."""
    for p in candidates:
        expanded = os.path.expanduser(str(p))
        if os.path.exists(expanded):
            return expanded
    return os.path.expanduser(str(candidates[0]))


# Candidate Claude memory directories on each device.
# Claude Code stores memory under ~/.claude/projects/<project-slug>/memory/.
# The slug for C:\Users\ohjos is "C--Users-ohjos" on Windows. On Linux it's
# usually "home-<user>" (e.g. "home-pi" or "home-ohjos").
POSSIBLE_CLAUDE_MEMORY_DIRS = [
    r"C:\Users\ohjos\.claude\projects\C--Users-ohjos\memory",          # desktop
    r"F:\.claude\projects\F-\memory",                                   # laptop (if claude runs from F:)
    os.path.expanduser(r"~\.claude\projects\C--Users-ohjos\memory"),   # windows fallback
    os.path.expanduser("~/.claude/projects/home-pi/memory"),            # raspie (pi user)
    os.path.expanduser("~/.claude/projects/home-ohjos/memory"),         # raspie (ohjos user)
    os.path.expanduser("~/.claude/projects/C--Users-ohjos/memory"),     # generic
]


def _load_device_registry() -> dict:
    """Load the hostname -> device name map from device_registry.json."""
    registry_path = Path(__file__).resolve().parent / "device_registry.json"
    if not registry_path.exists():
        return {"hostnames": {}, "fallback_order": ["desktop", "laptop", "raspie"]}
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"hostnames": {}, "fallback_order": ["desktop", "laptop", "raspie"]}


def detect_device() -> str:
    """Return 'desktop' / 'laptop' / 'raspie' / 'unknown'.

    Detection order:
      1. Hostname match in device_registry.json (most reliable).
      2. Filesystem heuristics as a fallback for brand-new devices.
    """
    registry = _load_device_registry()
    hostname = platform.node()

    # 1. Hostname lookup
    if hostname in registry.get("hostnames", {}):
        return registry["hostnames"][hostname]

    # 2. Filesystem fallback — only used when hostname isn't registered yet
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/etc/rpi-issue") or os.path.exists("/home/pi"):
            return "raspie"
        return "raspie"

    if system == "Windows":
        # Laptop is assumed when the portable F:\iCloudDrive setup is present
        # AND this script is running from an external drive.
        if os.path.exists(r"F:\iCloudDrive") and _running_from_external_drive():
            return "laptop"
        if os.path.exists(r"C:\Users\ohjos"):
            return "desktop"
        if os.path.exists(r"F:\iCloudDrive"):
            return "laptop"

    return "unknown"


def _running_from_external_drive() -> bool:
    r"""Heuristic: is this script being executed from F:\ / D:\ / E:\?"""
    try:
        here = Path(__file__).resolve()
        drive = str(here)[:2].upper()
        return drive in ("F:", "D:", "E:")
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent
MEMORY_SRC = REPO_ROOT / "memory"
SHARED_DIR = MEMORY_SRC / "shared"


def claude_memory_dir() -> Path:
    """Locate the Claude Code memory directory for this device."""
    # Environment override wins — useful on new machines where the default
    # candidate list doesn't match.
    override = os.environ.get("CLAUDE_MEMORY_DIR")
    if override:
        return Path(override)
    return Path(find_existing_path(POSSIBLE_CLAUDE_MEMORY_DIRS))


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def git(*args, check=True, capture=False):
    """Run a git command in the repo root."""
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        check=check,
        text=True,
        capture_output=capture,
    )
    return result


def _current_branch() -> str:
    try:
        return git("branch", "--show-current", capture=True).stdout.strip() or "master"
    except subprocess.CalledProcessError:
        return "master"


def git_pull():
    branch = _current_branch()
    print(f"[sync] git pull origin {branch}")
    git("pull", "origin", branch)


def git_commit_and_push(message: str):
    print("[sync] staging memory/ changes")
    git("add", "memory/")

    # Check if there's anything STAGED (not just modified in the working tree).
    # `git status --porcelain` can report files that autocrlf will normalize
    # back to identical once staged, leading to a spurious commit attempt.
    staged = git("diff", "--cached", "--name-only", "memory/", capture=True, check=False).stdout.strip()
    if not staged:
        print("[sync] nothing new to commit in memory/")
        return

    print(f"[sync] committing: {message}")
    git("commit", "-m", message)
    branch = _current_branch()
    print(f"[sync] git push origin {branch}")
    git("push", "origin", branch)


# ---------------------------------------------------------------------------
# Core sync actions
# ---------------------------------------------------------------------------

def iter_memory_files(folder: Path):
    if not folder.exists():
        return []
    return [p for p in folder.iterdir() if p.is_file() and p.suffix == ".md" and p.name != ".gitkeep"]


def pull_into_local(device: str, dry_run: bool = False) -> None:
    """Copy shared + device-specific memories from this repo into the local Claude memory dir."""
    dest = claude_memory_dir()
    print(f"[sync] device: {device}")
    print(f"[sync] target: {dest}")

    if not dest.exists():
        if dry_run:
            print(f"[sync] (dry-run) would create {dest}")
        else:
            dest.mkdir(parents=True, exist_ok=True)

    # 1) Copy shared memories
    shared_files = iter_memory_files(SHARED_DIR)
    # 2) Copy device-specific memories on top (later wins)
    device_dir = MEMORY_SRC / device
    device_files = iter_memory_files(device_dir)

    all_files = shared_files + device_files
    for src in all_files:
        target = dest / src.name
        action = "overwrite" if target.exists() else "create"
        print(f"  [{action}] {src.relative_to(REPO_ROOT)} -> {target}")
        if not dry_run:
            shutil.copy2(src, target)

    # 3) Rebuild MEMORY.md index from frontmatter descriptions
    index_path = dest / "MEMORY.md"
    lines = []
    for src in all_files:
        name, desc = _parse_frontmatter(src)
        hook = f"- [{name or src.stem}]({src.name}) — {desc or ''}".rstrip(" —")
        lines.append(hook)
    index_content = "\n".join(lines) + "\n"
    print(f"  [index]  {index_path} ({len(lines)} entries)")
    if not dry_run:
        index_path.write_text(index_content, encoding="utf-8")


def push_from_local(device: str, dry_run: bool = False) -> None:
    """Copy new/updated memory files from the local Claude memory dir back into this repo.

    Files go into memory/shared/ by default. To mark a file as device-specific,
    put it in the device folder by hand OR add a comment line
    `<!-- device: desktop -->` (or laptop / raspie) near the top of the file.
    """
    src_dir = claude_memory_dir()
    print(f"[sync] local source: {src_dir}")

    if not src_dir.exists():
        print("[sync] local Claude memory dir not found — nothing to push")
        return

    for src in iter_memory_files(src_dir):
        if src.name == "MEMORY.md":
            continue  # index is auto-generated; don't push it

        target_folder = _pick_target_folder(src, device)
        target = target_folder / src.name

        same = target.exists() and target.read_bytes() == src.read_bytes()
        if same:
            continue

        action = "update" if target.exists() else "add"
        print(f"  [{action}] {src} -> {target.relative_to(REPO_ROOT)}")
        if not dry_run:
            target_folder.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)


def _pick_target_folder(src: Path, device: str) -> Path:
    """Decide which memory subfolder a file belongs in when pushing up.

    A memory is routed to a device subfolder only if the file contains a line
    whose entire content (after stripping whitespace) equals
    ``<!-- device: desktop -->`` (or laptop / raspie). Matches inside inline
    code spans or prose are ignored so that documentation can describe the
    marker without triggering routing.
    """
    try:
        text = src.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        text = ""
    for raw_line in text.splitlines():
        line = raw_line.strip().lower()
        for candidate in ("desktop", "laptop", "raspie"):
            if line == f"<!-- device: {candidate} -->":
                return MEMORY_SRC / candidate
    return SHARED_DIR


def _parse_frontmatter(path: Path):
    """Pull name/description out of a memory file's YAML-ish frontmatter."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None, None
    if not text.startswith("---"):
        return None, None
    end = text.find("---", 3)
    if end == -1:
        return None, None
    header = text[3:end]
    name = None
    description = None
    for line in header.splitlines():
        line = line.strip()
        if line.lower().startswith("name:"):
            name = line.split(":", 1)[1].strip()
        elif line.lower().startswith("description:"):
            description = line.split(":", 1)[1].strip()
    return name, description


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else "")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--pull", action="store_true", help="(default) copy repo -> local Claude memory")
    group.add_argument("--push", action="store_true", help="copy local Claude memory -> repo")
    group.add_argument("--sync", action="store_true", help="git pull, then push local -> repo, then git commit+push")
    group.add_argument("--status", action="store_true", help="show detected device and paths")
    parser.add_argument("--dry-run", action="store_true", help="show actions without writing files")
    args = parser.parse_args()

    device = detect_device()
    dest = claude_memory_dir()

    if args.status:
        hostname = platform.node()
        registry = _load_device_registry()
        registered = hostname in registry.get("hostnames", {})
        print(f"hostname:     {hostname} {'(registered)' if registered else '(NOT registered — add to device_registry.json)'}")
        print(f"device:       {device}")
        print(f"repo root:    {REPO_ROOT}")
        print(f"memory src:   {MEMORY_SRC}")
        print(f"claude dest:  {dest}")
        shared = len(iter_memory_files(SHARED_DIR))
        specific = len(iter_memory_files(MEMORY_SRC / device))
        print(f"shared files: {shared}")
        print(f"{device} files: {specific}")
        return

    if args.sync:
        git_pull()
        push_from_local(device, dry_run=args.dry_run)
        pull_into_local(device, dry_run=args.dry_run)
        if not args.dry_run:
            git_commit_and_push(f"sync memory from {device}")
        return

    if args.push:
        push_from_local(device, dry_run=args.dry_run)
        return

    # default = pull
    try:
        git_pull()
    except subprocess.CalledProcessError as exc:
        print(f"[sync] git pull failed (continuing with local copy): {exc}")
    pull_into_local(device, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
