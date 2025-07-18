from fitness.workout import log_workout, view_workouts
from fitness.diet import log_meal, view_meals
from fitness.progress import show_summary

def menu():
    print("\n🏋️ Fitness Tracker")
    print("1. Log Workout")
    print("2. View Workouts")
    print("3. Log Meal")
    print("4. View Meals")
    print("5. Show Progress Summary")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            activity = input("Workout type: ")
            duration = int(input("Duration (min): "))
            log_workout(activity, duration)
        elif choice == "2":
            for w in view_workouts():
                print(w)
        elif choice == "3":
            food = input("Meal item: ")
            calories = int(input("Calories: "))
            log_meal(food, calories)
        elif choice == "4":
            for m in view_meals():
                print(m)
        elif choice == "5":
            show_summary()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
