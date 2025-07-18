from .exceptions import InvalidMarkException

def get_marks():
    marks = []
    subjects = int(input("Enter number of subjects: "))
    for i in range(subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        if not (0 <= mark <= 100):
            raise InvalidMarkException("Mark must be between 0 and 100.")
        marks.append(mark)
    return marks

def calculate_cgpa(marks):
    return round(sum(marks) / len(marks) / 9.5, 2)
