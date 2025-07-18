from .catalog import load_movies

def search_movie():
    keyword = input("Search keyword: ").strip().lower()
    movies = load_movies()

    found = [m for m in movies if keyword in m["title"].lower() or keyword in m["genre"].lower()]

    if found:
        print("\n🔍 Search Results:")
        for movie in found:
            print(f"🎥 {movie['title']} ({movie['year']}) - {movie['genre']} | ⭐ {movie['rating'] or 'N/A'}")
    else:
        print("🔎 No movies matched your search.")
