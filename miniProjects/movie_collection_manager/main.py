from movies.catalog import add_movie, list_movies
from movies.ratings import rate_movie
from movies.search import search_movie

if __name__ == "__main__":
    print("🎬 Movie Collection Manager 🎬")

    while True:
        print("\n1. Add Movie")
        print("2. List All Movies")
        print("3. Rate a Movie")
        print("4. Search Movie")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            list_movies()
        elif choice == "3":
            rate_movie()
        elif choice == "4":
            search_movie()
        elif choice == "5":
            print("👋 Exiting Movie Manager.")
            break
        else:
            print("❌ Invalid choice. Try again.")
