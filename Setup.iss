; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Fast Job Applier
AppVerName=Fast Job Applier --Version 0.5 ($Revision: 37 $)
AppPublisher=Blended Technologies, Inc.
AppPublisherURL=http://www.blendedtechnologies.com
AppSupportURL=http://www.blendedtechnologies.com
AppUpdatesURL=http://www.blendedtechnologies.com
DefaultDirName={pf}\Fast Job Applier
DefaultGroupName=Fast Job Applier
LicenseFile=C:\Documents and Settings\Gregory\My Documents\Get New Great Job\JobApplierMarkII\dist\COPYING
OutputDir=C:\Documents and Settings\Gregory\My Documents\Get New Great Job\JobApplierMarkII
OutputBaseFilename=Setup_FastJobApplier
Compression=lzma
SolidCompression=yes

[Languages]
Name: "eng"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Documents and Settings\Gregory\My Documents\Get New Great Job\JobApplierMarkII\dist\Fast_Job_Applier.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Gregory\My Documents\Get New Great Job\JobApplierMarkII\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Fast Job Applier"; Filename: "{app}\Fast_Job_Applier.exe"
Name: "{group}\{cm:UninstallProgram,Fast Job Applier}"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Fast Job Applier"; Filename: "{app}\Fast_Job_Applier.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Fast Job Applier"; Filename: "{app}\Fast_Job_Applier.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\Fast_Job_Applier.exe"; Description: "{cm:LaunchProgram,Fast Job Applier}"; Flags: nowait postinstall skipifsilent

