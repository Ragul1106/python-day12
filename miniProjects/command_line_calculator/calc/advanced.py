import math
from decimal import Decimal

def power(base, exp):
    return Decimal(base) ** Decimal(exp)

def sqrt(x):
    return Decimal(math.sqrt(float(x)))

def sin(x):
    return Decimal(math.sin(math.radians(float(x))))

def cos(x):
    return Decimal(math.cos(math.radians(float(x))))

def tan(x):
    return Decimal(math.tan(math.radians(float(x))))
