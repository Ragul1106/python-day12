import json
from math import floor

def show_summary():
    with open("fitness/storage.json", "r") as file:
        data = json.load(file)
        workouts = data.get("workouts", [])
        meals = data.get("meals", [])

    total_duration = sum(entry["duration"] for entry in workouts)
    total_calories = sum(entry["calories"] for entry in meals)
    workout_days = len(set(entry["date"] for entry in workouts))
    meal_days = len(set(entry["date"] for entry in meals))

    print("\n📈 Fitness Summary")
    print("-" * 30)
    print(f"🏃‍♂️ Total Workout Time: {total_duration} minutes")
    print(f"🥗 Total Calories Consumed: {total_calories} kcal")
    print(f"📅 Active Workout Days: {workout_days}")
    print(f"🍴 Meal Logged Days: {meal_days}")
    print("-" * 30)
