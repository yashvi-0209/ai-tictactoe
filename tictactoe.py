board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(' | '.join(row))
        if i < 2:
            print("-----")

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8),(2,4,6)]
    for i, j, k in wins:
        if b[i] == b[j] == b[k] and b[i] != ' ':
            return b[i]
    if ' ' not in b:
        return 'Draw'
    return None

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        else:
            print("Enter a number between 1 and 9.")

def minimax(b, is_maximizing, alpha, beta):
    winner = check_winner(b)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                eval = minimax(b, False, alpha, beta)
                b[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                eval = minimax(b, True, alpha, beta)
                b[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break 
        return min_eval

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False, -float('inf'), float('inf'))
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def game():
    print("Welcome to Tic Tac Toe.")
    print("You are X. AI is O.")
    print_board()

    while True:
        player_move()
        print_board()
        result = check_winner(board)
        if result:
            print(f"Game over: {result} wins!" if result != "Draw" else "It's a draw!")
            break

        print("AI's move:")
        ai_move()
        print_board()
        result = check_winner(board)
        if result:
            print(f"Game over: {result} wins!" if result != "Draw" else "It's a draw!")
            break

game()
