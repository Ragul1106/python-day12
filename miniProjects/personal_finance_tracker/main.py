from finance.income import add_income
from finance.expense import add_expense
from finance.summary import show_summary

def main():
    print("📒 Personal Finance Tracker")
    print("1. Add Income\n2. Add Expense\n3. Show Summary\n4. Exit")

    while True:
        choice = input("\nChoose an option: ")
        if choice == "1":
            try:
                amount = float(input("Enter income amount: ₹"))
                source = input("Enter income source: ")
                add_income(amount, source)
                print("✅ Income recorded.")
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: ₹"))
                category = input("Enter expense category: ")
                add_expense(amount, category)
                print("✅ Expense recorded.")
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
