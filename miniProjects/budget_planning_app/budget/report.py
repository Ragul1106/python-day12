import csv
from datetime import datetime
from math import ceil

BUDGET_FILE = "budget.csv"
EXPENSE_FILE = "expenses.csv"

def show_report():
    try:
        with open(BUDGET_FILE, 'r') as bf:
            reader = csv.DictReader(bf)
            budget_data = list(reader)[0]
            budget = float(budget_data["amount"])
            month = budget_data["month"]
    except (FileNotFoundError, IndexError, KeyError):
        print("⚠️ Budget not set yet!")
        return

    total_spent = 0
    expenses = []

    try:
        with open(EXPENSE_FILE, 'r') as ef:
            reader = csv.reader(ef)
            for row in reader:
                if len(row) >= 3:
                    date, category, amount = row[0], row[1], float(row[2])
                    total_spent += amount
                    expenses.append((date, category, amount, row[3] if len(row) > 3 else ""))
    except FileNotFoundError:
        print("📂 No expenses recorded.")
        return

    remaining = budget - total_spent

    print(f"\n📅 Monthly Report for {month}")
    print("-" * 50)
    print(f"{'Date':<12}{'Category':<15}{'Amount':<10}{'Note'}")
    print("-" * 50)
    for date, cat, amt, note in expenses:
        print(f"{date:<12}{cat:<15}₹{amt:<10.2f}{note}")
    
    print("-" * 50)
    print(f"💸 Total Spent: ₹{total_spent:.2f}")
    print(f"💰 Budget     : ₹{budget:.2f}")
    print(f"🧾 Remaining  : ₹{remaining:.2f}")
