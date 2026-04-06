@echo off
REM Removes the ClaudeMemorySync scheduled task.
set "TASK_NAME=ClaudeMemorySync"
schtasks /delete /tn "%TASK_NAME%" /f
if errorlevel 1 (
    echo Task was not registered.
) else (
    echo Task "%TASK_NAME%" removed.
)
