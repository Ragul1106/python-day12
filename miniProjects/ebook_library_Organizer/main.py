# main.py
from library.catalog import list_ebooks
from library.search import search_ebooks
from library.reader import read_ebook
import os

def main():
    while True:
        print("\n📚 eBook Library Organizer")
        print("1. List eBooks")
        print("2. Search in eBooks")
        print("3. Read an eBook")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            books = list_ebooks()
            print("\nAvailable eBooks:")
            for book in books:
                print(" -", book)
        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            results = search_ebooks(keyword)
            if results:
                print("\n🔍 Matches found in:")
                for book in results:
                    print(" -", book)
            else:
                print("❌ No matches found.")
        elif choice == "3":
            book = input("Enter book filename: ")
            read_ebook(book)
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
