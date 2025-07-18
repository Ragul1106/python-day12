# textutils/sanitize.py
import re
import string

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_numbers(text):
    return re.sub(r"\d+", "", text)
