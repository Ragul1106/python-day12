import calendar
from datetime import datetime
from .tasks import load_tasks

def view_calendar():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📅 Calendar View")
    now = datetime.now()
    print(calendar.month(now.year, now.month))

    print("🗓️ Tasks Due This Month:")
    for t in tasks:
        due_date = datetime.strptime(t["due"], "%Y-%m-%d")
        if due_date.year == now.year and due_date.month == now.month:
            print(f"- {due_date.day}: {t['title']} ({t['priority']})")
