import os
import shutil

def move_files(categorized, base_folder):
    for category, files in categorized.items():
        target_dir = os.path.join(base_folder, category)
        os.makedirs(target_dir, exist_ok=True)
        for file in files:
            filename = os.path.basename(file)
            target_path = os.path.join(target_dir, filename)
            if not os.path.exists(target_path):
                shutil.move(file, target_path)
