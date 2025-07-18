from finance.income import get_total_income
from finance.expense import get_total_expense

def show_summary():
    income = get_total_income()
    expense = get_total_expense()
    savings = income - expense

    print("\n📊 Financial Summary:")
    print(f"Total Income   : ₹{income:.2f}")
    print(f"Total Expenses : ₹{expense:.2f}")
    print(f"Savings        : ₹{savings:.2f}")
