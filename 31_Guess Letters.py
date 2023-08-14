def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman(word):
    guessed_letters = []
    correct_word = word.upper()
    guessed_word = display_word(correct_word, guessed_letters)
    
    while guessed_word != correct_word:
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in correct_word:
            guessed_letters.append(guess)
            guessed_word = display_word(correct_word, guessed_letters)
            print("Correct! Current progress:", guessed_word)
        else:
            guessed_letters.append(guess)
            print("Incorrect. Keep trying!")
    
    print("Congratulations! You guessed the word:", correct_word)

# Main game loop
if __name__ == "__main__":
    word_to_guess = "EVAPORATE"
    hangman(word_to_guess)