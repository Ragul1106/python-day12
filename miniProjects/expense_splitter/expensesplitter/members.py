from decimal import Decimal

group = {}

def add_member(name):
    if name not in group:
        group[name] = Decimal('0.00')

def add_expense(name, amount):
    from .helpers import validate_amount
    amount = validate_amount(amount)
    if name in group:
        group[name] += amount
    else:
        raise ValueError(f"{name} is not in the group")

def get_all_members():
    return group
