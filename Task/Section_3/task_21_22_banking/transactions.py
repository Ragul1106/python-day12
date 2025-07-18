def deposit(account, amount):
    account["balance"] += amount

def withdraw(account, amount):
    if account["balance"] >= amount:
        account["balance"] -= amount
    else:
        print("Insufficient balance.")
