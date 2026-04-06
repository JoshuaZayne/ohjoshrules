@echo off
REM Wrapper for the scheduled sync task.
REM Runs sync_memory.py --sync and logs output + exit code to sync_memory.log
REM Designed to be called by Windows Task Scheduler (see install_schedule.bat).

setlocal
cd /d "%~dp0"

set "LOG=%~dp0sync_memory.log"

REM Trim the log file if it's larger than ~1 MB so it doesn't grow forever.
for %%F in ("%LOG%") do (
    if exist "%%F" (
        if %%~zF GTR 1048576 del "%LOG%"
    )
)

>>"%LOG%" echo.
>>"%LOG%" echo ==================================================
>>"%LOG%" echo [%date% %time%] Starting sync on %COMPUTERNAME%
>>"%LOG%" echo ==================================================
python "%~dp0sync_memory.py" --sync >>"%LOG%" 2>&1
>>"%LOG%" echo [%date% %time%] Finished with exit code %errorlevel%

endlocal
