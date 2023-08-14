import random

def pick_random_word():
    with open("sowpods.txt", "r") as file:
        sowpods_words = file.readlines()

    random_word = random.choice(sowpods_words).strip()
    return random_word

# Call the function to get a random word
random_word = pick_random_word()
print("Random word:", random_word)