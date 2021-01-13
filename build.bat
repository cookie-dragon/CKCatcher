@echo off

pyinstaller.exe -w -n CKCatcher -i ico/icon.ico --version-file=file_version_info.txt --uac-admin --add-data="ui/res;res" main.py
