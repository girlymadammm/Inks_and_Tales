; Optional: makes a classic "Setup" installer with a wizard, Start menu icon and uninstaller.
; 1) Run build_exe.bat first.  2) Install the free Inno Setup (jrsoftware.org).  3) Open this file in it and press Compile.
[Setup]
AppName=Ink and Tales
AppVersion=1.0.0
AppPublisher=Ashki Studio
DefaultDirName={autopf}\Ink and Tales
DefaultGroupName=Ink and Tales
OutputDir=installer
OutputBaseFilename=Ink-and-Tales-Setup
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\Ink and Tales.exe
Compression=lzma
SolidCompression=yes
WizardStyle=modern
[Files]
Source: "dist\Ink and Tales.exe"; DestDir: "{app}"; Flags: ignoreversion
[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"
[Icons]
Name: "{group}\Ink and Tales"; Filename: "{app}\Ink and Tales.exe"
Name: "{autodesktop}\Ink and Tales"; Filename: "{app}\Ink and Tales.exe"; Tasks: desktopicon
[Run]
Filename: "{app}\Ink and Tales.exe"; Description: "Open Ink and Tales"; Flags: nowait postinstall skipifsilent
