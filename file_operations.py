# file_operations.py
import os
from tkinter import filedialog

def create_file(text_area):
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, 'w') as f:
            f.write("")
        text_area.insert("end", f"[Action]: Created file {filename}\n")

def open_file_from_desktop(text_area):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Desktop path
    filename = filedialog.askopenfilename(initialdir=desktop, title="Select file to open", filetypes=[("All files", "*.*")])
    if filename:
        os.startfile(filename)
        text_area.insert("end", f"[Action]: Opened file: {filename}\n")
