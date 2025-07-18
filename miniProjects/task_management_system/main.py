from taskmanager.tasks import add_task, list_tasks, update_task, delete_task
from taskmanager.calendar_view import view_calendar

if __name__ == "__main__":
    print("✅ Task Management System")

    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List All Tasks")
        print("5. Calendar View")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            view_calendar()
        elif choice == "6":
            print("👋 Exiting Task Manager.")
            break
        else:
            print("❌ Invalid choice.")
