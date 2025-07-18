from restaurant.menu import menu_items
from restaurant.offers import apply_discount

TAX_RATE = 0.05  # 5%

def calculate_bill(order):
    subtotal = sum(menu_items[item] * qty for item, qty in order.items())
    discount = apply_discount(subtotal)
    taxed_amount = (subtotal - discount) * TAX_RATE
    total = subtotal - discount + taxed_amount
    return subtotal, discount, taxed_amount, total

def print_bill(order_id, order, subtotal, discount, tax, total):
    print("\n📄 Final Bill")
    print("=" * 30)
    print(f"Order ID: {order_id}")
    print("Items Ordered:")
    for item, qty in order.items():
        print(f"  {item:10} x {qty:<2} = ₹{menu_items[item] * qty}")
    print("-" * 30)
    print(f"Subtotal       : ₹{subtotal:.2f}")
    print(f"Discount       : ₹{discount:.2f}")
    print(f"Tax (5%)       : ₹{tax:.2f}")
    print(f"Total Bill     : ₹{total:.2f}")
    print("=" * 30)
    print("🙏 Thank you for dining with us!")
