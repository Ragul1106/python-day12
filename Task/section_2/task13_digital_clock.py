import time
from datetime import datetime

def digital_clock():
    try:
        while True:
            print(datetime.now().strftime("%H:%M:%S"), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    digital_clock()
