# Ink and Tales: build it as a Windows app (.exe)
Made by **Ashki Studio**. This works the same way as your organizer app: a Python program that you turn into an .exe.

## How it works
`ink_and_tales.py` starts a small private server that only your own computer can reach, then opens the app in its own
window (Microsoft Edge, Chrome or Brave in "app mode", so there are no tabs or address bar). When you close the window,
everything stops. Nothing is sent over the internet. The app is the same full Ink and Tales you tried online.

## What you need (once)
- **Python 3.9 or newer** from python.org. During setup, tick **"Add Python to PATH"**.
- Microsoft Edge (already on Windows 10 and 11) or Chrome.

## Step 1: try it without building anything
Double-click **run_app.bat**. The app opens in its own window. Close the window to quit.

## Step 2: build the .exe
Double-click **build_exe.bat** and wait a minute or two. Your app appears at **dist\Ink and Tales.exe**.
Double-click it to open the app. You can copy that single file anywhere (Desktop, USB stick) or send it to your sister.

- Right-click the .exe and choose **Pin to taskbar** or **Send to, Desktop (create shortcut)**.
- If Windows shows **"Windows protected your PC"**, click **More info, then Run anyway**. This appears because the app is not
  signed with a paid certificate. If antivirus quarantines it, use **build_exe_folder.bat** instead (a folder version, which
  triggers fewer warnings) and open the .exe inside the `dist\Ink and Tales` folder.

## Optional: a proper "Setup" installer
Install the free **Inno Setup**, open **installer.iss** in it and press **Compile**. You get
`installer\Ink-and-Tales-Setup.exe` with a wizard, a Start menu icon and an uninstaller.

## Where your writing is saved
In `C:\Users\<you>\AppData\Local\InkAndTales\`. It stays when you close, update or reinstall the app.
It is separate from the website version and from other computers. To copy your writing between them, use
**Settings, Your data, Save backup** in one and **Restore backup** in the other. Make a backup now and then.
If something goes wrong when opening, a note is saved in `launcher.log` in that same folder.

## Updating the app later
Replace `app\index.html` with the new version, run **build_exe.bat** again, and use the new .exe. Your writing is kept.

## Phones
An .exe cannot run on a phone. On a phone use the online version and install it from the browser:
**Android** (Chrome menu, Install app) or **iPhone** (Safari, Share, Add to Home Screen).

## Mac and Linux
Run `python3 ink_and_tales.py` to open the app, or `build_app.sh` to build a Mac/Linux app.

## Files in this folder
| File | What it is |
|---|---|
| `ink_and_tales.py` | The launcher program |
| `app/` | The Ink and Tales app itself (page and icons) |
| `icon.ico` | The Ashki Studio feather icon for the .exe |
| `run_app.bat` | Opens the app without building |
| `build_exe.bat` / `build_exe_folder.bat` | Builds the .exe |
| `installer.iss` | Optional Setup installer recipe |
