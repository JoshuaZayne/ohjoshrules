@echo off
REM Registers a Windows scheduled task that runs scheduled_sync.bat at user logon.
REM
REM Usage:
REM   install_schedule.bat               (register at logon - default)
REM   install_schedule.bat /hourly       (register to run every hour instead)
REM   install_schedule.bat /daily 09:00  (register daily at 09:00)
REM
REM Run this ONCE per Windows device. It uses the current folder, so make sure
REM you run it from a permanent clone location (e.g. C:\Users\<user>\ohjoshrules)
REM and NOT from a USB drive that gets unplugged.

setlocal
set "TASK_NAME=ClaudeMemorySync"
set "WRAPPER=%~dp0scheduled_sync.bat"

if not exist "%WRAPPER%" (
    echo ERROR: scheduled_sync.bat not found next to install_schedule.bat
    exit /b 1
)

if "%~1"=="/hourly" (
    echo Registering %TASK_NAME% to run every hour from "%WRAPPER%"
    schtasks /create /tn "%TASK_NAME%" /tr "\"%WRAPPER%\"" /sc hourly /f
) else if "%~1"=="/daily" (
    if "%~2"=="" (
        echo ERROR: /daily requires a time argument like 09:00
        exit /b 1
    )
    echo Registering %TASK_NAME% to run daily at %~2 from "%WRAPPER%"
    schtasks /create /tn "%TASK_NAME%" /tr "\"%WRAPPER%\"" /sc daily /st %~2 /f
) else (
    echo Registering %TASK_NAME% to run at user logon from "%WRAPPER%"
    schtasks /create /tn "%TASK_NAME%" /tr "\"%WRAPPER%\"" /sc onlogon /f
)

if errorlevel 1 (
    echo FAILED to register scheduled task.
    exit /b 1
)

echo.
echo Scheduled task registered. To see it:
echo   schtasks /query /tn "%TASK_NAME%"
echo To remove it:
echo   uninstall_schedule.bat
echo To run it now for testing:
echo   schtasks /run /tn "%TASK_NAME%"
endlocal
