@echo off
cd /d %~dp0
copy hostnameOnTray.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
pause