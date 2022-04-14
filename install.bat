@echo off
title Remote Keylogger (Reborn)
cls
pip install --upgrade pip
pip install -r requirements.txt
pyfiglet "Remote Keylogger"
echo Remote Keylogger (Reborn)
echo Created by JahidFariz. Made with Love in India.
echo.
isort __main__.py
black __main__.py
echo.
rem :: https://www.windows-commandline.com/check-windows-32-bit-64-bit-command-line/
set architecture=%PROCESSOR_ARCHITECTURE%
pyinstaller __main__.py -F --add-data "fonts\\*;pyfiglet\fonts\\" --add-data "assets\\*;assets\\" -n=RKL_%architecture% -i="logo.ico" -y
echo.
del RKL_%architecture%.spec
rmdir /s /q __pycache__
rmdir /s /q build
echo.
python -c "from winsound import MessageBeep; MessageBeep()"
msg * Done . . .
pause
exit
