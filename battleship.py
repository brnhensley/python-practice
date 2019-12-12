from random import randint

board = []
display_board = []

for x in range(0, 10):
    display_board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)
    print

def random_position(board, ship_size):
    starting_pos = [randint(0, len(board) - 1), randint(0, len(board) - 1)]
    direction = randint(0,1) # 0 = Left Right, 1 = Up Down

    i = 0
    if direction == 0: # left - right
        if ship_size < len(board) - starting_pos[1]:
            # Ship goes right
            while i < ship_size:
                board[starting_pos[0]][starting_pos[1] + i] = "1"
                i += 1
        else:
            # ship goes left
            while i < ship_size:
                board[starting_pos[0]][starting_pos[1] - i] = "1"
                i += 1
    else:   # up down
        if ship_size < len(board) - starting_pos[0]:
            # ship goes Down
            while i < ship_size:
                board[starting_pos[0] + i][starting_pos[1]] = "1"
                i += 1
        else:
            #  ship goes up
            while i < ship_size:
                board[starting_pos[0] - i][starting_pos[1]] = "1"
                i += 1
    return board

def guess():
    guess = []
    guess.append(int(raw_input("Guess Row: ")) - 1)
    guess.append(int(raw_input("Guess Col: ")) - 1)
    update_board(guess)

def update_board(user_guess):
    if board[user_guess[0]][user_guess[1]] == "1":
        print "\nIt's a hit!\n"
        board[user_guess[0]][user_guess[1]] = "X"
    else:
        print "You missed my battleship!\n"
        board[user_guess[0]][user_guess[1]] = "#"
    print_board(board)
    check_win()

def check_win():
    win = True
    for row in board:
        if "1" in row:
            win = False
    if not win:
        guess()
    else:
        print "YOU FUCKING SANK MY BATTLESHIP! \n"


board = random_position(display_board, randint(2,6))
print_board(board)
guess()