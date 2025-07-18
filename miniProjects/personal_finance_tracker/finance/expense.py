import json, os
from datetime import datetime

expense_file = "expense.json"

def add_expense(amount, category):
    entry = {"amount": amount, "category": category, "date": datetime.now().isoformat()}
    data = []
    if os.path.exists(expense_file):
        with open(expense_file, "r") as f:
            data = json.load(f)
    data.append(entry)
    with open(expense_file, "w") as f:
        json.dump(data, f, indent=4)

def get_total_expense():
    if not os.path.exists(expense_file):
        return 0
    with open(expense_file, "r") as f:
        data = json.load(f)
    return sum(item["amount"] for item in data)
