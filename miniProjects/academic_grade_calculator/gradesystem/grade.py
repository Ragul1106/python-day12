def get_grade(cgpa):
    if cgpa >= 9.0:
        return 'A+'
    elif cgpa >= 8.0:
        return 'A'
    elif cgpa >= 7.0:
        return 'B'
    elif cgpa >= 6.0:
        return 'C'
    elif cgpa >= 5.0:
        return 'D'
    else:
        return 'F'
