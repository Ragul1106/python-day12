import json
from datetime import datetime

def log_workout(activity, duration_minutes):
    date = datetime.now().strftime("%Y-%m-%d")
    workout_entry = {"date": date, "activity": activity, "duration": duration_minutes}

    with open("fitness/storage.json", "r+") as file:
        data = json.load(file)
        data["workouts"].append(workout_entry)
        file.seek(0)
        json.dump(data, file, indent=4)

def view_workouts():
    with open("fitness/storage.json", "r") as file:
        data = json.load(file)
        return data.get("workouts", [])
