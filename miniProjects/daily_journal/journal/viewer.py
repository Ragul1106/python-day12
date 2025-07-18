import os

def view_entries(date=None):
    path = "journal_data"
    if date:
        filename = os.path.join(path, f"{date}.txt")
        if not os.path.exists(filename):
            print("⚠️ No entry found for this date.")
            return
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        for file in sorted(os.listdir(path)):
            if file.endswith(".txt"):
                print(f"\n📅 {file.replace('.txt', '')}")
                print("-" * 80)
                with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                    print(f.read())
