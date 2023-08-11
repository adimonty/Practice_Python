def reverse_words_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string