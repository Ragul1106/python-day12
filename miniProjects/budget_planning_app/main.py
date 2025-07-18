from budget.planner import set_budget
from budget.tracker import add_expense
from budget.report import show_report

if __name__ == "__main__":
    print("📊 Welcome to Budget Planning App")
    while True:
        print("\n1. Set Monthly Budget")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            set_budget()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            show_report()
        elif choice == '4':
            print("✅ Exiting Budget App.")
            break
        else:
            print("❌ Invalid choice.")
