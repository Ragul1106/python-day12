import random
from restaurant.menu import menu_items

def generate_order_id():
    return f"ORD{random.randint(1000, 9999)}"

def take_order():
    order = {}
    print("\n🔽 Enter your order (type 'done' to finish):")
    while True:
        item = input("Item: ").title()
        if item == "Done":
            break
        if item in menu_items:
            qty = int(input("Quantity: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("❌ Item not on menu.")
    return order
