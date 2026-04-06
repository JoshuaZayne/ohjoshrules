@echo off
REM Windows wrapper for sync_memory.py
REM Usage: sync_memory.bat            (pull from github into local Claude memory)
REM        sync_memory.bat --push     (push local memory up to repo)
REM        sync_memory.bat --sync     (full round-trip: pull, push local, commit+push)
REM        sync_memory.bat --status   (show device detection)
python "%~dp0sync_memory.py" %*
