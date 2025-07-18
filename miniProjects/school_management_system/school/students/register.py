import json, os

student_file = "students.json"

def register_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    data = []
    if os.path.exists(student_file):
        with open(student_file, "r") as f:
            data = json.load(f)
    data.append(student)
    with open(student_file, "w") as f:
        json.dump(data, f, indent=4)
