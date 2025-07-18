import random

def guess_game():
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Correct!")
    else:
        print(f"Wrong! The number was {number}")

if __name__ == "__main__":
    guess_game()
