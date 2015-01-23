import re

def sentence_split(text):
    return re.split(r"[?.!]\s+", text)
