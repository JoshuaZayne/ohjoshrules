' run_hidden.vbs — launches a command with NO visible window.
' Used by Windows Task Scheduler to run .bat scripts without flashing an
' empty cmd.exe window into the interactive session.
'
' Usage:  wscript.exe run_hidden.vbs "C:\path\to\script.bat" [extra args...]
'
' Waits for the child to finish (so Task Scheduler sees the real duration)
' and returns the child's exit code so the task's LastTaskResult is accurate.
Option Explicit
Dim sh, cmd, i, q
q = Chr(34)
Set sh = CreateObject("WScript.Shell")
cmd = q & WScript.Arguments(0) & q
For i = 1 To WScript.Arguments.Count - 1
  cmd = cmd & " " & q & WScript.Arguments(i) & q
Next
' Window style 0 = hidden, True = wait for completion.
WScript.Quit sh.Run(cmd, 0, True)
