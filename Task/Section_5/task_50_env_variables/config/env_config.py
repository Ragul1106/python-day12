from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def show_config():
    return {
        "API_KEY": API_KEY,
        "DB_USER": DB_USER,
        "DB_PASS": DB_PASS
    }
