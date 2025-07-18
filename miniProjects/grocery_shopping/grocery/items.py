ITEMS = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 25,
    "rice": 60,
    "eggs": 6
}

def get_price(item):
    return ITEMS.get(item.lower())

def show_items():
    print("\n🛍️  Available Grocery Items")
    for name, price in ITEMS.items():
        print(f"{name.capitalize():10} - ₹{price}")
