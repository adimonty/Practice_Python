import random

number = random.randint(1, 9)
number_of_guesses = 0

while True:
    guess = input("Guess a number between 1 and 9: ")

    if not guess.isdigit():
        print("Please enter a valid number between 1 and 9.")
        continue

    guess = int(guess)

    if guess < 1 or guess > 9:
        print("Please enter a number between 1 and 9.")
        continue

    number_of_guesses += 1

    if guess == number:
        break

print(f"You needed {number_of_guesses} guesses to guess the number {number}")
