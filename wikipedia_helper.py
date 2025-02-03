import wikipedia
from text_to_speech import speak

def get_wikipedia_summary(topic, text_area):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        text_area.insert("end", f"[Wikipedia Summary for '{topic}']: {summary}\n")
        speak(summary)
    except Exception as e:
        text_area.insert("end", f"[Error retrieving Wikipedia summary]: {e}\n")
