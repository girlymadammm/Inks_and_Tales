@echo off
rem Same app, but as a folder instead of one file. It starts faster and Windows Defender complains less.
setlocal
cd /d "%~dp0"
python -m pip install --upgrade pyinstaller
if errorlevel 1 goto :fail
python -m PyInstaller --noconfirm --clean --onedir --windowed --name "Ink and Tales" --icon icon.ico --add-data "app;app" ink_and_tales.py
if errorlevel 1 goto :fail
echo.
echo  Done! Your app is in the folder:   dist\Ink and Tales\   (open "Ink and Tales.exe" inside it)
echo.
pause
exit /b 0
:fail
echo  Something went wrong. Please copy the messages above and send them to Claude.
pause
exit /b 1
