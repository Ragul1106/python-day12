def generate_report(group, balances, total):
    print("\n📄 Expense Report")
    print("-" * 30)
    print(f"Total Expense: ₹{total}")
    for name, paid in group.items():
        print(f"{name:10} paid ₹{paid}")

    print("\n💸 Settlement Summary:")
    for name, balance in balances.items():
        if balance < 0:
            print(f"{name} owes ₹{abs(balance)}")
        elif balance > 0:
            print(f"{name} is owed ₹{balance}")
        else:
            print(f"{name} is settled")
