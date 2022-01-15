#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

OnMessage(0x219, "notify_change") 
return 

notify_change(wParam, lParam, msg, hwnd) 
{
	;outputdebug notify_change(%wParam%, %lParam%, %msg%, %hwnd%) 
	if msg = 537
		Run, launch.bat
		Sleep, 1500
}