import argparse
from filemanager.scan import scan_directory
from filemanager.move import move_files
from filemanager.report import print_report

def main():
    parser = argparse.ArgumentParser(description="📁 File Organizer Tool")
    parser.add_argument("folder", help="Path to folder to organize")

    args = parser.parse_args()
    folder_path = args.folder

    print(f"\n🔍 Scanning: {folder_path}")
    categorized = scan_directory(folder_path)

    print("🚚 Moving files...")
    move_files(categorized, folder_path)

    print_report(categorized)

if __name__ == "__main__":
    main()
