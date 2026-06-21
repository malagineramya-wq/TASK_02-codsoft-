import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'

def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move!")
        except:
            print("Enter a valid number!")

while True:
    print_board()
    human_move()

    if check_winner('X'):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break