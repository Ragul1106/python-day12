from journal.entry import add_entry
from journal.viewer import view_entries
from journal.exporter import export_all, search_notes

def menu():
    print("""
📝 Daily Journal App
----------------------
1. Add New Entry
2. View All Entries
3. View Specific Date
4. Search Keyword
5. Export Journal
6. Exit
""")

def main():
    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            note = input("Write your note:\n> ")
            add_entry(note)
        elif choice == '2':
            view_entries()
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            view_entries(date)
        elif choice == '4':
            keyword = input("Enter keyword to search: ")
            search_notes(keyword)
        elif choice == '5':
            export_all()
        elif choice == '6':
            print("👋 Exiting Journal. Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
