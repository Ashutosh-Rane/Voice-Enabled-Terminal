import sys
import io
import psutil
import os
import webbrowser
from text_to_speech import speak
import subprocess

def execute_python_code(command, text_area):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    local_vars = {}
    exec(command, {}, local_vars)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    if output.strip():
        text_area.insert("end", f"[Python Output]: {output.strip()}\n")
    else:
        text_area.insert("end", "[Python Output]: None\n")

def show_response(response, text_area):
    text_area.insert("end", f"[Response]: {response}\n")
    speak(response)

def perform_system_actions(command, text_area):
    if "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        text_area.insert("end", "[Action]: Opening YouTube...\n")
    elif "open calculator" in command.lower():
        subprocess.Popen("calc.exe")
        text_area.insert("end", "[Action]: Opening Calculator...\n")
    elif "open notepad" in command.lower():
        subprocess.Popen("notepad.exe")
        text_area.insert("end", "[Action]: Opening Notepad...\n")
    elif "check disk space" in command.lower():
        disk_usage = psutil.disk_usage("/")
        response = f"Disk Space: {disk_usage.percent}% used"
        show_response(response, text_area)
    elif "check cpu usage" in command.lower():
        cpu_usage = psutil.cpu_percent(interval=1)
        response = f"CPU Usage: {cpu_usage}%"
        show_response(response, text_area)
    else:
        text_area.insert("end", "[Error]: Command not recognized.\n")
