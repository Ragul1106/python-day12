# library/catalog.py
import os
import glob
from .config import EBOOK_DIR

def list_ebooks():
    if not os.path.exists(EBOOK_DIR):
        print("No eBook directory found.")
        return []

    ebooks = glob.glob(os.path.join(EBOOK_DIR, "*.txt"))
    return [os.path.basename(book) for book in ebooks]
