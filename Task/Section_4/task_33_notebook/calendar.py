from datetime import datetime
def show_today():
    print(f"Today is {datetime.today().strftime('%A, %d %B %Y')}")
