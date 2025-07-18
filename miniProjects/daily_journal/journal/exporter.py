import os
import fnmatch
import re

def export_all(output_file="full_journal.txt"):
    with open(output_file, "w", encoding="utf-8") as out:
        for file in sorted(os.listdir("journal_data")):
            if file.endswith(".txt"):
                out.write(f"\n=== {file.replace('.txt', '')} ===\n")
                with open(os.path.join("journal_data", file), "r", encoding="utf-8") as f:
                    out.write(f.read())
    print(f"📤 Journal exported to {output_file}")

def search_notes(keyword):
    pattern = re.compile(keyword, re.IGNORECASE)
    for file in os.listdir("journal_data"):
        if fnmatch.fnmatch(file, "*.txt"):
            with open(os.path.join("journal_data", file), "r", encoding="utf-8") as f:
                content = f.read()
                if pattern.search(content):
                    print(f"\n🔎 Found in {file}:")
                    print("-" * 80)
                    for line in content.splitlines():
                        if pattern.search(line):
                            print(line.strip())
