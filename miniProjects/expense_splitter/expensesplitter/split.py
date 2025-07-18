from decimal import Decimal

def calculate_split(group):
    total = sum(group.values())
    members = len(group)
    if members == 0:
        return {}, Decimal('0.00')
    equal_share = total / members
    balances = {name: round(paid - equal_share, 2) for name, paid in group.items()}
    return balances, total
