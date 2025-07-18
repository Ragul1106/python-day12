import csv
from datetime import datetime

BUDGET_FILE = "budget.csv"

def set_budget():
    month = datetime.now().strftime("%B %Y")
    amount = float(input(f"Enter budget for {month}: ₹"))
    
    with open(BUDGET_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["month", "amount"])
        writer.writerow([month, amount])
    
    print(f"✅ Budget of ₹{amount:.2f} set for {month}")
