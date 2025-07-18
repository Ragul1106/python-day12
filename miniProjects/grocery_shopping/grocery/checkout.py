import json
import random
from datetime import datetime

def generate_bill(cart, prices):
    bill_id = f"BILL{random.randint(1000, 9999)}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = 0
    items = []

    for item, qty in cart.items():
        price = prices.get(item, 0)
        subtotal = qty * price
        total += subtotal
        items.append({
            "item": item,
            "qty": qty,
            "price": price,
            "subtotal": subtotal
        })

    bill_data = {
        "bill_id": bill_id,
        "timestamp": timestamp,
        "items": items,
        "total": total
    }

    with open(f"{bill_id}.json", "w") as f:
        json.dump(bill_data, f, indent=4)

    print(f"\n✅ Bill generated successfully! ID: {bill_id}")
    print(f"🧾 Total Payable: ₹{total}")
    return bill_data
