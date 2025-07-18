from datetime import datetime
from payroll.salary import calculate_basic_salary
from payroll.tax import calculate_tax

def generate_payslip(employee):
    basic = calculate_basic_salary(employee.position)
    tax = calculate_tax(basic)
    net = basic - tax
    date = datetime.now().strftime("%Y-%m-%d")

    slip = (
        f"🧾 Payslip - {date}\n"
        f"----------------------------\n"
        f"Employee ID   : {employee.emp_id}\n"
        f"Name          : {employee.name}\n"
        f"Position      : {employee.position}\n"
        f"Basic Salary  : ₹{basic}\n"
        f"Tax Deducted  : ₹{tax}\n"
        f"Net Salary    : ₹{net}\n"
        f"----------------------------\n"
    )
    return slip
