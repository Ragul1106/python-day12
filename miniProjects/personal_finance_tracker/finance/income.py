import json, os
from datetime import datetime

income_file = "income.json"

def add_income(amount, source):
    entry = {"amount": amount, "source": source, "date": datetime.now().isoformat()}
    data = []
    if os.path.exists(income_file):
        with open(income_file, "r") as f:
            data = json.load(f)
    data.append(entry)
    with open(income_file, "w") as f:
        json.dump(data, f, indent=4)

def get_total_income():
    if not os.path.exists(income_file):
        return 0
    with open(income_file, "r") as f:
        data = json.load(f)
    return sum(item["amount"] for item in data)
