---
name: project_c_drive_space_cleanup
description: "C: drive filled to 6 GB free (2026-08-05) — the WSL crash-dump cause, the reusable cleanup script, and what is still large"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7692375f-e49d-4ed1-8bc1-03287f3594d3
  modified: 2026-08-06T04:51:53.160Z
---

On 2026-08-05 the desktop's C: (3,723 GB) was down to **6.3 GB free**. Cleared to **641 GB free** in one session.

**Root cause worth remembering: `%TEMP%\wsl-crashes` held 261 GB in just 10 `.dmp` files.** WSL writes a full memory dump when a process crashes inside it, and retains **10 by default**. Playwright Chromium was crash-looping, and each browser dump is multi-GB. Nothing warns you and nothing cleans it up.

**Fix applied:** created `C:\Users\ohjos\.wslconfig` with `maxCrashDumpCount=2` under `[wsl2]` (set `0` to disable dumps entirely). **Requires `wsl --shutdown` to take effect.** If C: fills again unexpectedly, check `%TEMP%\wsl-crashes` FIRST.

**Reusable tool: `C:\Users\ohjos\Scripts\Clear-TempSpace.ps1`.** Report-only by default; `-Execute` to delete. Flags: `-IncludeCaution` (adds conda/npm/pip/NuGet/Yarn caches), `-MinimumAgeDays N` (skips recently-touched files, use 1+ for routine runs), `-Targets '<name>'` (single location). Targets are tagged Safe vs Caution, locked files are skipped not forced, and nested targets are reported separately but not double-counted. Run elevated to also clear `C:\Windows\Temp` and the Windows Update cache. First run reclaimed 278.8 GB.

**Gotchas hit:** `Remove-Item -Recurse` leaves partial trees on long paths and reserved names; the working fallback is `cmd /c "rd /s /q \\?\<path>"`. Also, a safety hook blocks commands where `robocopy /MIR` and `Remove-Item` appear together (it misparses `/MIR` as a path), so do not combine them in one call.

**Still large on C: (2026-08-05, after cleanup):** `iCloudPhotos` ~1,002 GB, `C:\Ohjoshrules` ~289 GB, `Music` ~207 GB, `Videos` ~139 GB, `.ollama` models ~78 GB, `Documents` ~62 GB, `VirtualBox VMs` ~39 GB. Adobe temp (~3 GB) could not be cleared because AdobeUpdateService and the notification clients hold it open. The 366 GB of iCloudReorg stage mirrors were deleted separately — see [[project_icloud_reorg]].
