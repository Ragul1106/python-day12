from expensesplitter.members import add_member, add_expense, get_all_members
from expensesplitter.split import calculate_split
from expensesplitter.report import generate_report

if __name__ == "__main__":
    print("👥 Expense Splitter for Groups\n")

    num = int(input("Enter number of members: "))
    for _ in range(num):
        name = input("Enter member name: ")
        add_member(name)

    while True:
        name = input("\nEnter name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if name not in get_all_members():
            print("❌ Member not found!")
            continue
        try:
            amount = input("Enter amount paid: ")
            add_expense(name, amount)
        except ValueError as e:
            print(e)

    group = get_all_members()
    balances, total = calculate_split(group)
    generate_report(group, balances, total)
