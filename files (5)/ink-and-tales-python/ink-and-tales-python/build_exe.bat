@echo off
setlocal
cd /d "%~dp0"
echo.
echo  Ink and Tales: building the Windows app (.exe)
echo  ---------------------------------------------
echo  Step 1 of 2: getting the packaging tool (only needed the first time)...
python -m pip install --upgrade pyinstaller
if errorlevel 1 goto :fail
echo.
echo  Step 2 of 2: building the app. This takes a minute or two...
python -m PyInstaller --noconfirm --clean --onefile --windowed --name "Ink and Tales" --icon icon.ico --add-data "app;app" ink_and_tales.py
if errorlevel 1 goto :fail
echo.
echo  Done! Your app is here:   dist\Ink and Tales.exe
echo  Double-click it to open Ink and Tales. You can copy it anywhere, or send it to your sister.
echo.
pause
exit /b 0
:fail
echo.
echo  Something went wrong. Please copy the messages above and send them to Claude.
echo.
pause
exit /b 1
