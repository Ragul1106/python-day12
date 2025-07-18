from tax import calc_tax
from profit import calc_profit
from loss import calc_loss

revenue = 5000
cost = 3000
print("Profit:", calc_profit(revenue, cost))
print("Tax:", calc_tax(revenue))
print("Loss:", calc_loss(cost, revenue))
