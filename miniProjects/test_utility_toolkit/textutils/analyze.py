# textutils/analyze.py
from .count import count_words, count_chars, count_lines
from .sanitize import remove_punctuation
from .utils import to_lower

def summary(text):
    clean_text = to_lower(remove_punctuation(text))
    return {
        "words": count_words(clean_text),
        "characters": count_chars(clean_text),
        "lines": count_lines(clean_text)
    }
