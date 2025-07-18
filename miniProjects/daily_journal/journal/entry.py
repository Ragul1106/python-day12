import os
from datetime import datetime
import textwrap

DATA_DIR = "journal_data"

def add_entry(note: str):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(DATA_DIR, f"{date_str}.txt")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- {datetime.now().strftime('%H:%M:%S')} ---\n")
        f.write(textwrap.fill(note, width=80) + "\n")
    
    print(f"✅ Note added to {filename}")
