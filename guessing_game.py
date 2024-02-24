import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (Hint: It is between 0 - 100)\n"))
        attempts += 1
        if guess < number:
            print("Too low, try again")
        elif guess > number:
            print("Too high, try again")
        else:
            print(f"Congratulations! Guessed right in {attempts} attempts")
            break

number_guessing_game()