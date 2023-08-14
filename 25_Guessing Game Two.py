def binary_search_guess(user_number):
    low = 0
    high = 100
    guesses = 0
    
    while True:
        guess = (low + high) // 2
        guesses += 1
        
        print(f"Is your number {guess}? (higher / lower / correct): ")
        feedback = input().lower()
        
        if feedback == "correct":
            return guesses
        elif feedback == "higher":
            low = guess + 1
        elif feedback == "lower":
            high = guess - 1

def main():
    print("Think of a number between 0 and 100 (inclusive).")
    input("Press Enter when you're ready to start...")
    
    user_number = int(input("Enter the number you're thinking of: "))
    
    guesses = binary_search_guess(user_number)
    
    print(f"I guessed your number in {guesses} guesses!")

if __name__ == "__main__":
    main()
