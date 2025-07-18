import math

def calculate_tax(salary):
    if salary <= 25000:
        return 0
    elif salary <= 50000:
        return math.ceil(salary * 0.05)
    elif salary <= 75000:
        return math.ceil(salary * 0.1)
    else:
        return math.ceil(salary * 0.15)
