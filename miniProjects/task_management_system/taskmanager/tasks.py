import json
from datetime import datetime
from .priority import choose_priority

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Task Title: ")
    due_date = input("Due Date (YYYY-MM-DD): ")
    priority = choose_priority()

    task = {
        "id": datetime.now().timestamp(),
        "title": title,
        "due": due_date,
        "priority": priority,
        "done": False
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📋 Your Tasks:")
    print("-" * 50)
    for t in tasks:
        status = "✅" if t["done"] else "❌"
        print(f"{status} {t['title']} | Due: {t['due']} | Priority: {t['priority']}")
    print("-" * 50)

def update_task():
    list_tasks()
    task_id = input("Enter title of task to update: ").strip()

    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["title"].lower() == task_id.lower():
            t["done"] = input("Mark as done? (yes/no): ").lower() == 'yes'
            t["priority"] = choose_priority()
            found = True
            break

    if found:
        save_tasks(tasks)
        print("🔁 Task updated.")
    else:
        print("⚠️ Task not found.")

def delete_task():
    list_tasks()
    task_title = input("Enter title of task to delete: ").strip()

    tasks = load_tasks()
    updated = [t for t in tasks if t["title"].lower() != task_title.lower()]
    
    if len(updated) != len(tasks):
        save_tasks(updated)
        print("🗑️ Task deleted.")
    else:
        print("⚠️ Task not found.")
