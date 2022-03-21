#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

OnMessage(0x219, "notify_change") 
return 

notify_change(wParam, lParam, msg, hwnd) 
{
	if msg = 537
		Run, launch.bat
		Sleep, 3500
		Reload, %A_ScriptDir%\launch.ahk
}
