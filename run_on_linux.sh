#!/bin/bash
if [ -d "myenv" ]; then
    source myenv/bin/activate
    python3 password.py
else
    python3 -m venv myenv
    source myenv/bin/activate
    python3 -m pip install pyperclip >/dev/null
    python3 password.py
fi