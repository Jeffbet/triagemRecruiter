; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=RecruiterScOpe
AppVersion=1.0
DefaultDirName={pf}\RecruiterScOpe
OutputDir=Output
OutputBaseFilename=RecruiterScOpe_Setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "C:\Users\ariel\OneDrive\Documentos\�rea de Desenvolvimento\triagem\dist\triagem.exe"; DestDir: "{app}"
; Outros arquivos/diret�rios que pode incluir

[Icons]
Name: "{group}\RecruiterScOpe"; Filename: "{app}\RecruiterScOpe.exe"

[Setup]
; Aqui adiciono uma imagem como logo da instala��o
WizardImageFile=C:\Users\ariel\OneDrive\Documentos\�rea de Desenvolvimento\triagem\recruitterS1.bmp
WizardSmallImageFile=C:\Users\ariel\OneDrive\Documentos\�rea de Desenvolvimento\triagem\recruitterS2.bmp