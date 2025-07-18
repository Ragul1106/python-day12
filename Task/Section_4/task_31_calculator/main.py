from add import add
from sub import subtract
from mul import multiply
from div import divide

print("Calculator")
a, b = 10, 5
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")
