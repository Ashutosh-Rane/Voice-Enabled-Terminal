# media_control.py
import pywhatkit

def play_song(command, text_area):
    song_name = command[5:].strip()
    text_area.insert("end", f"[Action]: Playing {song_name} on YouTube...\n")
    pywhatkit.playonyt(song_name)  # Play the song on YouTube
