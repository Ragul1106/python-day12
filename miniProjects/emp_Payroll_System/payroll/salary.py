def calculate_basic_salary(position):
    base_salaries = {
        "Manager": 80000,
        "Developer": 60000,
        "Designer": 50000,
        "Intern": 20000
    }
    return base_salaries.get(position, 30000)
