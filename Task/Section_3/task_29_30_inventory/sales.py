from .stock import update_stock 

def sell_item(item, qty):
    print(f"Selling {qty} units of {item}")
    update_stock(item, -qty)
