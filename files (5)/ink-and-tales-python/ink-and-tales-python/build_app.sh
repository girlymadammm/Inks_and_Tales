#!/bin/sh
# Mac / Linux version of build_exe.bat
cd "$(dirname "$0")"
python3 -m pip install --upgrade pyinstaller || exit 1
python3 -m PyInstaller --noconfirm --clean --onefile --windowed --name "Ink and Tales" --add-data "app:app" ink_and_tales.py || exit 1
echo "Done! Your app is in the dist folder."
