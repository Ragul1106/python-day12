# main.py
from payroll.employee import Employee
from payroll.payslip import generate_payslip

def main():
    print("💼 Employee Payroll System")
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    position = input("Enter position (Manager, Developer, Designer, Intern): ")

    emp = Employee(emp_id, name, position)
    slip = generate_payslip(emp)
    print("\n" + slip)

if __name__ == "__main__":
    main()
