from school.students.register import register_student
from school.teachers.register import register_teacher
from school.subjects.assign import assign_subject
from school.report import show_report

def main():
    print("🏫 School Management System")
    print("1. Register Student")
    print("2. Register Teacher")
    print("3. Assign Subject")
    print("4. Show Report")
    print("5. Exit")

    while True:
        choice = input("\nChoose an option: ")
        if choice == "1":
            name = input("Student name: ")
            age = input("Student age: ")
            grade = input("Grade: ")
            register_student(name, age, grade)
            print("✅ Student registered.")
        elif choice == "2":
            name = input("Teacher name: ")
            subject = input("Subject: ")
            register_teacher(name, subject)
            print("✅ Teacher registered.")
        elif choice == "3":
            subject = input("Subject name: ")
            teacher = input("Assign to teacher: ")
            assign_subject(subject, teacher)
            print("✅ Subject assigned.")
        elif choice == "4":
            show_report()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
