def display_report(marks, cgpa, grade):
    print("\n📋 Grade Report")
    print("-" * 30)
    for i, mark in enumerate(marks, 1):
        print(f"Subject {i}: {mark}")
    print(f"\nCGPA: {cgpa}")
    print(f"Grade: {grade}")
    print("-" * 30)
