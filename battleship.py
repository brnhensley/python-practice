from random import randint

display_board = []
play_board = []
x = 8
for space in range(0, x):
    display_board.append(["O"] * x)
    play_board.append(["O"] * x)

def print_board(board_to_print):
    for row in board_to_print:
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
    guess_row = int(raw_input("GUESS ROW: ")) - 1
    guess_col = int(raw_input("GUESS COL: ")) - 1
    return guess_row, guess_col

def update_board(row, col):
    if row not in range(0, x) or col not in range(0, x):
        print "\nGUESS OUT OF BOUNDS, TRY AGAIN\n"
    else:
        if play_board[row][col] == "1":
            print "\nIT'S A HIT!\n"
            play_board[row][col] = "X"
            display_board[row][col] = "X"
        elif play_board[row][col] == "#" or play_board[row][col] == "X":
            print "\nYOU ALREADY TRIED THAT SPACE! \nGUESS AGAIN"
        else:
            print "\nYOU MISSED!\n"
            play_board[row][col] = "#"
            display_board[row][col] = "#"

def check_win():
    win = True
    for row in play_board:
        if "1" in row:
            win = False
    return win

play_board = random_position(play_board, randint(2,6))

for turn in range(0,10):
    print_board(display_board)
    row, col = guess()
    update_board(row, col)
    if check_win():
        print_board(play_board)
        print "YOU SANK MY BATTLESHIP! \nYOU WIN"
        break

print "OUT OF TURNS, YOU LOSE\n"
print_board(play_board)