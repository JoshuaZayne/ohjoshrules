"""
Machine and drive detection for per-machine gitignore rules.

Reuses the canonical device registry that already lives next to
ohjoshrules/sync_memory.py so every tool in this repo uses the same
hostname -> device name mapping.

Run directly to print what this machine is identified as:
    python detect.py
"""
import json
import os
import platform
import socket
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEVICE_REGISTRY = REPO_ROOT / "device_registry.json"


def get_hostname():
    """Return the hostname as-is (case preserved to match registry keys)."""
    return os.environ.get("COMPUTERNAME") or socket.gethostname() or ""


def _load_registry():
    if not DEVICE_REGISTRY.exists():
        return {"hostnames": {}, "fallback_order": ["desktop", "laptop", "raspie"]}
    try:
        with open(DEVICE_REGISTRY, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"hostnames": {}, "fallback_order": ["desktop", "laptop", "raspie"]}


def get_machine():
    """
    Return a short canonical machine identifier
    ('desktop', 'laptop', 'raspie', or 'unknown').

    Resolution order:
      1. Exact hostname match in device_registry.json.
      2. Case-insensitive hostname match (tolerant of the Windows habit of
         uppercasing COMPUTERNAME).
      3. OS + drive signature fallback.
    """
    host = get_hostname()
    registry = _load_registry()
    hostnames = registry.get("hostnames", {})

    if host in hostnames:
        return hostnames[host]
    # case-insensitive fallback
    lower_map = {k.lower(): v for k, v in hostnames.items()}
    if host.lower() in lower_map:
        return lower_map[host.lower()]

    # OS + drive signature fallback
    system = platform.system()
    if system == "Linux":
        if os.path.exists("/etc/rpi-issue") or os.path.exists("/home/pi"):
            return "raspie"
        return "raspie"
    if system == "Windows":
        if os.path.exists(r"C:\Users\ohjos") and os.path.exists(r"D:\Code"):
            return "desktop"
        if os.path.exists(r"F:\iCloudDrive"):
            return "laptop"
        return "unknown"

    return "unknown"


def check_drives():
    """
    Verify expected drives/paths for the current OS.
    Returns a list of (path, exists) tuples and prints a summary.
    """
    system = platform.system()
    if system == "Windows":
        expected = [r"C:\\", r"D:\\", r"F:\\", r"C:\Users\ohjos", r"D:\Code"]
    elif system == "Linux":
        expected = [str(Path.home()), "/media", "/home/pi"]
    else:
        expected = []

    results = []
    print("--- Drive / path check ---")
    for p in expected:
        ok = os.path.exists(p)
        results.append((p, ok))
        mark = "OK " if ok else "MISS"
        print(f"  [{mark}] {p}")
    return results


def find_repos(search_roots, max_depth=4):
    """
    Find all git repos under the given search roots.
    A repo is any directory containing a .git subdirectory.
    Depth is measured from each search root.
    """
    repos = []
    for root in search_roots:
        root = Path(root)
        if not root.exists():
            continue
        for git_dir in root.rglob(".git"):
            if not git_dir.is_dir():
                continue
            try:
                depth = len(git_dir.relative_to(root).parts)
            except ValueError:
                continue
            if depth <= max_depth:
                repos.append(git_dir.parent.resolve())
    seen = set()
    unique = []
    for r in repos:
        if r not in seen:
            seen.add(r)
            unique.append(r)
    return unique


if __name__ == "__main__":
    print(f"Hostname:  {get_hostname()}")
    print(f"System:    {platform.system()}")
    print(f"Machine:   {get_machine()}")
    print(f"Registry:  {DEVICE_REGISTRY}")
    print()
    check_drives()
