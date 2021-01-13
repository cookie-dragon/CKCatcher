#!/bin/sh

pyinstaller -Fw -n CKCatcher -i ico/icon.icns --osx-bundle-identifier="tk.cooky.ckcatcher" --add-data="ui/res:res" main.py
