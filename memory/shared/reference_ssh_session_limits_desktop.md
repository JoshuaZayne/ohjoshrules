---
name: reference-ssh-session-limits-desktop
description: "Claude sessions reached over SSH on the desktop (DimaskusPC) run in Windows session 0: no stored GitHub sign in, and only the machine PATH unless the PowerShell profile adds the user PATH"
metadata:
  node_type: memory
  type: reference
  originSessionId: 022194cd-3266-49fa-94df-aeca0a8d6280
  modified: 2026-11-14T07:09:22.469Z
---

When the user reaches the desktop (DimaskusPC) over SSH, Claude runs under sshd in Windows session 0 (process chain sshd-session, conhost, powershell, claude). Seen 2026-11-13 and 14:

1. The Windows credential list is empty there (`cmdkey /list` shows NONE), so `git push` over https fails with "could not read Password" and `gh` reports its sign in failed. The SSH keys in `~/.ssh` are not GitHub keys. Pushes must be run by the user from a desktop terminal (or after a `gh auth login` there).
2. The shell gets only the machine PATH, not the user PATH (cargo, npm, anaconda env folders and others are missing). On 2026-11-14 a block was added at the end of the PowerShell profile (`Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`, backup `_before_2026-11-14_000905`) that adds the missing user PATH folders; Claude must be started again from a new shell to pick it up.
3. rust-analyzer was installed as a rustup component (stable and 1.99.1) on 2026-11-14 for the Claude Code rust-analyzer plugin; the RustTOS `rust-toolchain.toml` was not changed.

Related: [[project_rusttos]], [[project_ssh_setup]].
