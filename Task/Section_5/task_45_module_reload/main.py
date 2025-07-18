
import mod 
print(mod.greet())

import time
import importlib
print("Modify mod.py and press Enter")
input()
importlib.reload(mod)
print(mod.greet())