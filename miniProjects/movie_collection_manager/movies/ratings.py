from .catalog import load_movies, save_movies

def rate_movie():
    title = input("Enter movie title to rate: ").strip()
    movies = load_movies()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            rating = input("Give rating (1-5): ")
            if rating.isdigit() and 1 <= int(rating) <= 5:
                movie["rating"] = int(rating)
                save_movies(movies)
                print("🌟 Rating added!")
                return
            else:
                print("⚠️ Invalid rating. Use 1 to 5.")
                return

    print("❌ Movie not found.")
