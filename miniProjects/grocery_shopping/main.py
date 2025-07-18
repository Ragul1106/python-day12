from grocery.items import show_items, get_price, ITEMS
from grocery.cart import add_to_cart, remove_from_cart, view_cart, get_cart
from grocery.checkout import generate_bill

def main():
    print("🛒 Welcome to Meenu's Grocery Store!")

    while True:
        print("\n1. Show Items\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_items()

        elif choice == '2':
            item = input("Enter item name: ").lower()
            if item not in ITEMS:
                print("❌ Item not available.")
                continue
            try:
                qty = int(input("Enter quantity: "))
                add_to_cart(item, qty)
            except:
                print("❌ Invalid quantity")

        elif choice == '3':
            item = input("Enter item name to remove: ").lower()
            remove_from_cart(item)

        elif choice == '4':
            view_cart(ITEMS)

        elif choice == '5':
            cart = get_cart()
            if not cart:
                print("🪣 Cart is empty!")
            else:
                generate_bill(cart, ITEMS)
                break

        elif choice == '6':
            print("👋 Thank you for shopping!")
            break

        else:
            print("❗ Invalid choice")

if __name__ == "__main__":
    main()
