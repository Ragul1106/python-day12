# library/search.py
import re
from .catalog import list_ebooks
from .config import EBOOK_DIR
import os

def search_ebooks(keyword):
    matches = []
    for book in list_ebooks():
        path = os.path.join(EBOOK_DIR, book)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            if re.search(keyword, content, re.IGNORECASE):
                matches.append(book)
    return matches
