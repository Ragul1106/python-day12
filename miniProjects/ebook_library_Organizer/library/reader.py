# library/reader.py
import os
from .config import EBOOK_DIR

def read_ebook(book_name):
    path = os.path.join(EBOOK_DIR, book_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            print(f"📖 Reading: {book_name}\n")
            print(f.read(1000))  # preview first 1000 chars
    else:
        print("❌ Book not found.")
