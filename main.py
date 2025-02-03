import tkinter as tk
from terminal_emulator import TerminalEmulator

if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalEmulator(root)
    root.mainloop()
