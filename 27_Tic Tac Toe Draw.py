# Initialize the game board
gameboard = [(['.']*3) for _ in range(3)]

# Variables for input and turn count
row_col = [0]
turn = 1

# Checks if the input is valid
# - that it is in the format "row,col"
# - that the position is free
def input_valid(values):
    # Input has only two values
    if len(values) != 2:
        print("Input must be two numbers in format row,col e.g. 1,2")
        return False
    # Input is a number between 1 and 3 (inclusive)
    try:
        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
            # Checks if the position on the board is already filled
            if gameboard[int(values[0])-1][int(values[1])-1] != '.':
                print("Position on the board is already taken.")
                return False
            return True
        else:
            print("Input values must be numbers between 1 and 3 (inclusive)")
            return False
    except ValueError:
        print("Input values must be numbers between 1 and 3 (inclusive)")
        return False

# Draws the board
def draw_board(values, player):
    # Changes the value to X or O
    gameboard[int(values[0])-1][int(values[1])-1] = player

    # Print the gameboard
    for row in gameboard:
        print(' '.join(row))

# Checks if the game is over (no more '.' or there is a winner)
def game_over():
    searcht = '.'

    # Check win by row
    for i in range(3):
        if len(set(gameboard[i])) == 1 and gameboard[i][1] != searcht:
            print("Game over - Player", gameboard[i][1], "wins")
            return True

    # Check win by column
    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i] and gameboard[0][i] != searcht:
            print("Game over - Player", gameboard[0][i], "wins")
            return True

    # Check win by diagonal
    if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2] or gameboard[0][2] == gameboard[1][1] == gameboard[2][0]) and gameboard[1][1] != searcht:
        print("Game over - Player", gameboard[1][1], "wins")
        return True

    # Check if the board is full
    for sublist in gameboard:
        if searcht in sublist:
            return False

    print("Game over - the board is filled")
    return True

# Main function that runs the game while the board is not full
while not game_over():
    piece = '.'

    # Player input - checks for input correctness
    while not input_valid(row_col):
        player = turn % 2
        if player == 0:
            player = 2
            piece = 'O'
        else:
            piece = 'X'
        p1 = input('Player ' + str(player) + ' input: ')
        row_col = p1.split(",")

    draw_board(row_col, piece)

    row_col = [0]
    turn += 1
