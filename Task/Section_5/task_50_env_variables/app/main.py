from config.env_config import API_KEY, DB_USER, DB_PASS, show_config

def connect_to_service():
    print(f"[INFO] Connecting with API_KEY: {API_KEY}")
    print(f"[INFO] Logging in with DB_USER: {DB_USER}")

def run_app():
    connect_to_service()
    print("\n[CONFIG SUMMARY]")
    for key, val in show_config().items():
        print(f"{key}: {val}")

if __name__ == "__main__":
    run_app()
