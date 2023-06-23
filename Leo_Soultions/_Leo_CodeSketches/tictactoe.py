# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win():
    # Define the possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    # Check if any winning combination is filled with X or O
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return True

    return False

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()

        # Get the current player's move
        if current_player == 'X':
            position = int(input('Player X, choose a position (1-9): ')) - 1
        else:
            position = int(input('Player O, choose a position (1-9): ')) - 1

        # Update the board
        if board[position] == ' ':
            board[position] = current_player
        else:
            print('That position is already taken. Try again.')
            continue

        # Check for a win
        if check_win():
            display_board()
            print('Player', current_player, 'wins!')
            game_over = True
        # Check for a draw
        elif check_draw():
            display_board()
            print('It\'s a draw!')
            game_over = True
        else:
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
