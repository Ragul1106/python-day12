from restaurant.menu import display_menu
from restaurant.order import generate_order_id, take_order
from restaurant.bill import calculate_bill, print_bill

if __name__ == "__main__":
    print("🍽️ Welcome to Meenu's Restaurant!")
    display_menu()
    
    order = take_order()
    
    if not order:
        print("⚠️ No items ordered.")
    else:
        order_id = generate_order_id()
        subtotal, discount, tax, total = calculate_bill(order)
        print_bill(order_id, order, subtotal, discount, tax, total)
