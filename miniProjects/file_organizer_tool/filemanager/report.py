def print_report(categorized):
    print("\n📂 File Organization Report")
    print("-" * 30)
    for category, files in categorized.items():
        print(f"{category}: {len(files)} files")
