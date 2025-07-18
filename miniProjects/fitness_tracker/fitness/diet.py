import json
from datetime import datetime

def log_meal(food, calories):
    date = datetime.now().strftime("%Y-%m-%d")
    meal_entry = {"date": date, "food": food, "calories": calories}

    with open("fitness/storage.json", "r+") as file:
        data = json.load(file)
        data["meals"].append(meal_entry)
        file.seek(0)
        json.dump(data, file, indent=4)

def view_meals():
    with open("fitness/storage.json", "r") as file:
        data = json.load(file)
        return data.get("meals", [])
