insert_revision_info.py
rmdir /S /Q dist
rmdir /S /Q build
C:\Python24\python.exe setup.py py2exe
"C:\Program Files\Inno Setup 5\Compil32.exe" /cc Setup.iss
C:\Python24\python.exe setup.py bdist_wininst
pause