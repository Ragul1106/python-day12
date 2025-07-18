from gradesystem.marks import get_marks, calculate_cgpa
from gradesystem.grade import get_grade
from gradesystem.report import display_report
from gradesystem.exceptions import InvalidMarkException

if __name__ == "__main__":
    print("🎓 Academic Grade Calculator 🎓")
    try:
        marks = get_marks()
        cgpa = calculate_cgpa(marks)
        grade = get_grade(cgpa)
        display_report(marks, cgpa, grade)
    except InvalidMarkException as e:
        print(f"❌ Error: {e}")
    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")
