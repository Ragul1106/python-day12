import json, os

def show_report():
    print("📚 School Report")

    print("\n👩‍🎓 Students:")
    if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            for s in json.load(f):
                print(f"{s['name']} (Age {s['age']}) - Grade {s['grade']}")

    print("\n👨‍🏫 Teachers:")
    if os.path.exists("teachers.json"):
        with open("teachers.json", "r") as f:
            for t in json.load(f):
                print(f"{t['name']} teaches {t['subject']}")

    print("\n📖 Subjects:")
    if os.path.exists("subjects.json"):
        with open("subjects.json", "r") as f:
            for sub in json.load(f):
                print(f"{sub['subject']} assigned to {sub['teacher']}")
