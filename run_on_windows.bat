@echo off
if exist myenv (
    call myenv\Scripts\activate.bat
    python password.py
    pause
) else (
    python -m venv myenv
    call myenv\Scripts\activate.bat
    python -m pip install pyperclip >NUL
    python password.py
    pause
)