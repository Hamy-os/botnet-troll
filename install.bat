@echo off
cd /d "%~dp0"
set "inst_dir=%temp%\temp_installer"
mkdir "%inst_dir%">nul 2>&1
echo %0\..\
copy /Y %0\..\main.exe "%inst_dir%"
pause