import csv
from datetime import datetime

EXPENSE_FILE = "expenses.csv"

def add_expense():
    category = input("Expense Category: ")
    amount = float(input("Amount Spent: ₹"))
    note = input("Note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    
    print(f"🧾 Recorded ₹{amount:.2f} in '{category}'")
