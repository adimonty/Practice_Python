import random

def pick_random_word():
    with open("sowpods.txt", "r") as file:
        sowpods_words = file.readlines()

    random_word = random.choice(sowpods_words).strip()
    return random_word

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts_left):
    hangman_art = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        """
    ]
    
    return hangman_art[6 - attempts_left]

def hangman(word):
    guessed_letters = []
    correct_word = word.upper()
    guessed_word = display_word(correct_word, guessed_letters)
    guesses_left = 6
    
    while guessed_word != correct_word and guesses_left > 0:
        print(draw_hangman(guesses_left))
        guess = input(f"Guess a letter (guesses left: {guesses_left}): ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in correct_word:
            guessed_letters.append(guess)
            guessed_word = display_word(correct_word, guessed_letters)
            print("Correct! Current progress:", guessed_word)
        else:
            guessed_letters.append(guess)
            guesses_left -= 1
            print("Incorrect. Keep trying!")
    
    if guessed_word == correct_word:
        print("Congratulations! You guessed the word:", correct_word)
    else:
        print(draw_hangman(0))
        print("Out of guesses. The word was:", correct_word)
    
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

# Main game loop
if __name__ == "__main__":
    play_again = True
    
    while play_again:
        random_word = pick_random_word()
        print("Random word:", random_word)
        
        play_again = hangman(random_word)
    
    print("Thanks for playing Hangman!")
