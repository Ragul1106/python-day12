import pickle
import os
from datetime import datetime

MOVIE_FILE = "movies.pkl"

def load_movies():
    if os.path.exists(MOVIE_FILE):
        with open(MOVIE_FILE, "rb") as f:
            return pickle.load(f)
    return []

def save_movies(movies):
    with open(MOVIE_FILE, "wb") as f:
        pickle.dump(movies, f)

def add_movie():
    title = input("Enter movie title: ")
    genre = input("Genre: ")
    year = input("Release year: ")

    movie = {
        "title": title,
        "genre": genre,
        "year": year,
        "rating": None,
        "added_on": datetime.now().strftime("%Y-%m-%d")
    }

    movies = load_movies()
    movies.append(movie)
    save_movies(movies)
    print("✅ Movie added successfully!")

def list_movies():
    movies = load_movies()
    if not movies:
        print("📭 No movies in your collection.")
        return

    print("\n🎞️ Your Movie List:")
    print("-" * 40)
    for movie in movies:
        print(f"🎬 {movie['title']} ({movie['year']}) - {movie['genre']} | ⭐ {movie['rating'] or 'Not Rated'}")
    print("-" * 40)
