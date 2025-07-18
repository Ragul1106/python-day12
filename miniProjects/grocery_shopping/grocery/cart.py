cart = {}

def add_to_cart(item, quantity):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

def remove_from_cart(item):
    if item in cart:
        del cart[item]

def view_cart(prices):
    print("\n🧺 Your Cart:")
    total = 0
    for item, qty in cart.items():
        price = prices.get(item, 0)
        subtotal = qty * price
        total += subtotal
        print(f"{item.capitalize():10} x {qty:<3} = ₹{subtotal}")
    print(f"🧾 Total Amount: ₹{total}")
    return total

def get_cart():
    return cart
