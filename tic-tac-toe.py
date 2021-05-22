board = ["-","-","-",
    "-","-","-",
    "-","-","-",]
game_still_going_on = True
winner = None
current_player = 'X'

def display_board():
    print('\n')
    print(board[0]+" | "+board[1]+" | "+board[2]+" | ")
    print(board[3]+" | "+board[4]+" | "+board[5]+" | ")
    print(board[6]+" | "+board[7]+" | "+board[8]+" | ")
    print('\n')

def play_game():
    display_board()
    while game_still_going_on:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print(player+"'s turn")
    position = int(input("Enter a position from 1-9: "))
    valid = True
    while valid:
        while position not in [1,2,3,4,5,6,7,8,9]:
            position = int(input("Invalid number, Please choose position from 1-9: "))
        position = position-1
        if board[position]=='-':
            valid = False
    board[position]=player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    global winner
    row_winner = check_row()
    col_winner = check_column()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner=col_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_row():
    global game_still_going_on
    row_1 = board[0] == board[1] == board[2]!='-'
    row_2 = board[3] == board[4] == board[5]!='-'
    row_3 = board[6] == board[7] == board[8]!='-'
    if row_1 or row_2 or row_3:
        game_still_going_on=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[4]
    else:
        return None

def check_column():
    global game_still_going_on
    col_1 = board[0] == board[3] == board[6]!='-'
    col_2 = board[1] == board[4] == board[7]!='-'
    col_3 = board[2] == board[5] == board[8]!='-'
    if col_1 or col_2 or col_3:
        game_still_going_on=False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def check_diagonal():
    global game_still_going_on
    diagonal_1 = board[0] == board[4] == board[8]!='-'
    diagonal_2 = board[2] == board[4] == board[6]!='-'
    if diagonal_1 or diagonal_2:
        game_still_going_on=False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    else:
        return None

def check_for_tie():
    global game_still_going_on
    if "-" not in board:
        game_still_going_on=False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

if __name__ == '__main__':
    play_game()