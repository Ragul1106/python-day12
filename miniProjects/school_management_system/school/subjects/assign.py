import json, os

subject_file = "subjects.json"

def assign_subject(subject_name, teacher_name):
    subject = {"subject": subject_name, "teacher": teacher_name}
    data = []
    if os.path.exists(subject_file):
        with open(subject_file, "r") as f:
            data = json.load(f)
    data.append(subject)
    with open(subject_file, "w") as f:
        json.dump(data, f, indent=4)
