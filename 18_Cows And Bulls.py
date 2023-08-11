import random

def compare_numbers(secret, guess):
    cows = 0
    bulls = 0
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            cows += 1
        elif secret[i] in guess:
            bulls += 1
    
    return cows, bulls

def main():
    secret_number = str(random.randint(1000, 9999))
    num_guesses = 0
    
    print("Welcome to the Cows and Bulls game!")
    print("Try to guess the 4-digit number.")
    
    while True:
        user_guess = input("Enter your guess: ")
        
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        num_guesses += 1
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {num_guesses} guesses.")
            break
        
        cows, bulls = compare_numbers(secret_number, user_guess)
        print(f"Cows: {cows}, Bulls: {bulls}")

if __name__ == "__main__":
    main()
