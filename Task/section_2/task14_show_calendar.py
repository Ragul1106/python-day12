import calendar
from datetime import datetime

year = datetime.now().year
month = datetime.now().month

print(calendar.month(year, month))
