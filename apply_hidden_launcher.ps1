<#
apply_hidden_launcher.ps1 — stop scheduled tasks from flashing empty cmd windows.

Windows Task Scheduler must spawn a visible cmd.exe window to host a .bat/.cmd
action that runs in an interactive logon session. This script finds those tasks
and repoints them through run_hidden.vbs (in this same folder), which runs the
batch hidden via wscript.exe while still waiting for it and returning its exit
code. Same script, same credentials, same schedule — just no window.

Safe to re-run: tasks already routed through wscript.exe are skipped.
Run it in a normal (non-admin) PowerShell — it only touches your own user tasks.

    powershell -ExecutionPolicy Bypass -File apply_hidden_launcher.ps1
#>

$vbs = Join-Path $PSScriptRoot 'run_hidden.vbs'
if (-not (Test-Path $vbs)) {
    Write-Error "run_hidden.vbs not found next to this script ($vbs). Sync the repo first."
    exit 1
}

$changed = 0
Get-ScheduledTask | Where-Object {
    $_.TaskPath -notmatch '^\\Microsoft\\' -and
    $_.State -ne 'Disabled' -and
    $_.Principal.LogonType -eq 'Interactive'
} | ForEach-Object {
    $task = $_
    $act  = $task.Actions | Select-Object -First 1
    if (-not $act -or -not $act.Execute) { return }

    $exe = $act.Execute
    # Already wrapped? skip.
    if ($exe -match 'wscript\.exe$') { return }

    # Case A: action directly runs a .bat/.cmd
    # Case B: action runs cmd.exe /c "something.bat"
    $target = $null; $targetArgs = $null
    if ($exe -match '\.(bat|cmd)"?$') {
        $target = $exe.Trim('"'); $targetArgs = $act.Arguments
    }
    elseif ($exe -match 'cmd\.exe$' -and $act.Arguments -match '\.(bat|cmd)') {
        $target = $exe; $targetArgs = $act.Arguments   # wrap the whole cmd invocation
    }
    if (-not $target) { return }

    $argLine = '"{0}" "{1}"' -f $vbs, $target
    if ($targetArgs) { $argLine += ' ' + $targetArgs }

    $newAct = New-ScheduledTaskAction -Execute 'wscript.exe' -Argument $argLine `
        -WorkingDirectory $act.WorkingDirectory
    Set-ScheduledTask -TaskName $task.TaskName -TaskPath $task.TaskPath -Action $newAct | Out-Null
    Write-Host ("[fixed] {0}{1}  ->  hidden" -f $task.TaskPath, $task.TaskName) -ForegroundColor Green
    $changed++
}

if ($changed -eq 0) {
    Write-Host "Nothing to change — no interactive .bat/.cmd tasks found (or all already hidden)." -ForegroundColor Yellow
} else {
    Write-Host ("Done. {0} task(s) will now run without a visible window." -f $changed) -ForegroundColor Cyan
}
