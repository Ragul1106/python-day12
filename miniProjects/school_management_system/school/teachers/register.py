import json, os

teacher_file = "teachers.json"

def register_teacher(name, subject):
    teacher = {"name": name, "subject": subject}
    data = []
    if os.path.exists(teacher_file):
        with open(teacher_file, "r") as f:
            data = json.load(f)
    data.append(teacher)
    with open(teacher_file, "w") as f:
        json.dump(data, f, indent=4)
