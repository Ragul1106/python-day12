from .cart import cart

def calculate_total():
    return sum(item['price'] for item in cart)
