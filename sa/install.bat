echo %inst_dir%
cd /d "%~dp0"
set "inst_dir=%temp%\temp_installer"
mkdir "%inst_dir%">nul 2>&1
copy /Y main.exe "%inst_dir%"
REM call the created file
start "" "%temp%\temp_installer\main.exe"
call "%inst_dir%\main.exe" /S
pause