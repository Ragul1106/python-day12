import os
import glob

FILE_TYPES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Music": ['.mp3', '.wav'],
    "Archives": ['.zip', '.rar', '.tar'],
    "Scripts": ['.py', '.js', '.html', '.css']
}

def scan_directory(directory):
    categorized = {category: [] for category in FILE_TYPES}
    categorized["Others"] = []

    for filepath in glob.glob(os.path.join(directory, '*')):
        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filepath)
            ext = ext.lower()
            placed = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    categorized[category].append(filepath)
                    placed = True
                    break
            if not placed:
                categorized["Others"].append(filepath)
    return categorized
