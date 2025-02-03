import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import webbrowser
import subprocess
import os
import io
import sys
import utilities  # Imports for utility functions
from voice_recognition import recognize_voice
from wikipedia_helper import get_wikipedia_summary
from text_to_speech import speak  # Text-to-speech functionality
import pywhatkit
import psutil
from file_operations import create_file, open_file_from_desktop
from media_control import play_song
import torch



class TerminalEmulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Terminal Emulator")
        


        # Text area for displaying output
        self.text_area = scrolledtext.ScrolledText(
            self.root, width=80, height=20, wrap=tk.WORD, bg="#282c34", fg="#ffffff", font=("Consolas", 12)
        )
        self.text_area.pack(fill="both", expand=True)
        self.text_area.insert("1.0", "Welcome to the Enhanced Terminal Emulator!\n")
        self.text_area.config(state="disabled")

        # Input field and frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", pady=5)
        self.input_field = tk.Entry(input_frame, width=60, bg="#3e4451", fg="#ffffff", font=("Consolas", 12))
        self.input_field.pack(side="left", fill="x", padx=10, expand=True)
        self.input_field.bind("<Return>", self.execute_command)
        self.submit_button = tk.Button(input_frame, text="Submit", command=self.submit_command, bg="#61afef", activebackground="#98c379", font=("Consolas", 12))
        self.submit_button.pack(side="left", padx=10)
        self.help_button = tk.Button(input_frame, text="Help", command=self.show_help, bg="#61afef", activebackground="#98c379", font=("Consolas", 12))
        self.help_button.pack(side="left", padx=10)

        # Voice button
        self.voice_button = tk.Button(self.root, text="🎤 Speak Command", command=self.recognize_voice_command, bg="#61afef", activebackground="#98c379", font=("Consolas", 12))
        self.voice_button.pack(pady=10)

        # Text-to-speech engine greeting
        speak("Hello! I'm your virtual assistant. How can I assist you today?")

    def submit_command(self):
        command = self.input_field.get()
        self.input_field.delete(0, "end")
        self.process_command(command)

    def execute_command(self, event):
        self.submit_command()

    def process_command(self, command):
        self.text_area.config(state="normal")
        self.text_area.insert("end", "====================\n")
        self.text_area.insert("end", f"Command: {command}\n")
        self.text_area.insert("end", "====================\n")
        speak(f"Executing command: {command}")

        try:
            if any(op in command for op in ['+', '-', '*', '/']):
                result = eval(command)
                self.text_area.insert("end", f"[Arithmetic Result]: {result}\n")
            elif command.startswith("print") or "=" in command or "import" in command:
                utilities.execute_python_code(command, self.text_area)
            elif "how are you" in command.lower():
                utilities.show_response("I'm just a program, but thanks for asking! How can I help you today?", self.text_area)
            elif "what can you do" in command.lower():
                utilities.show_response("I can open applications, execute commands, perform arithmetic operations, and more. What would you like me to do?", self.text_area)
            elif "tell me a joke" in command.lower():
                utilities.show_response("Why did the computer cross the road? To get to the other side!", self.text_area)
            elif "tell me about" in command.lower() or "what is" in command.lower() or "who is" in command.lower():
                topic = command.split("about")[-1].strip() if "about" in command else command.split("is")[-1].strip()
                get_wikipedia_summary(topic, self.text_area)
            elif "search for" in command.lower():
                query = command.split("search for")[-1].strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")
                self.text_area.insert("end", f"[Action]: Searching for '{query}' on Google...\n")
            elif command.lower().startswith("play"):
                play_song(command, self.text_area)  # Add this line for playing songs
            elif command.lower().startswith("create file"):
                create_file(self.text_area)
            elif command.lower().startswith("open file"):
                open_file_from_desktop(self.text_area)
            else:
                utilities.perform_system_actions(command, self.text_area)

        except Exception as e:
            self.text_area.insert("end", f"[Error]: {e}\n")
        self.text_area.config(state="disabled")






    def recognize_voice_command(self):
        command = recognize_voice()
        if command:
            self.text_area.config(state="normal")
            self.text_area.insert("end", f"[Voice Command]: {command}\n")
            self.text_area.config(state="disabled")
            self.process_command(command)
            
    

    

    def show_help(self):
        help_text = (
            "Available Commands:\n"
            "1. How are you\n"
            "2. What can you do\n"
            "3. Tell me a joke\n"
            "4. Search for [topic]\n"
            "5. Tell me about [topic]\n"
            "6. Play [song name]\n"
            "7. Open explorer\n"
            "8. Create file\n"
            "9. Open [application name] (e.g., notepad, calculator)\n"
            "10. Check disk space\n"
            "11. Check CPU usage\n"
            "12. Weather for [location]\n"
            "13. Execute Python code (e.g., print('Hello World!'))\n"
        )
        messagebox.showinfo("Help", help_text)
