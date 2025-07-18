from decimal import Decimal

def validate_amount(amount):
    try:
        return Decimal(str(amount))
    except:
        raise ValueError("Invalid amount. Must be a number.")
