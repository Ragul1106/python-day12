menu_items = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Fries": 100,
    "Coke": 50
}

def display_menu():
    print("🧾 Available Menu:\n")
    for item, price in menu_items.items():
        print(f"{item:10} - ₹{price}")
