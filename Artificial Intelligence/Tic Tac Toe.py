import random

# Function to print the board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to evaluate the board for the AI player
def evaluate(board):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    else:
        return 0

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth+1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth+1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function for the AI player to make a move
def ai_move(board):
    best_move = None
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "X"


board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
    
while True:
        # Player's move
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
    if board[row][col] == " ":
        board[row][col] = "O"
    else:
        print("Invalid move, try again.")
        continue
        
    print_board(board)
        
        # Check if player has won
    if check_win(board, "O"):
        print("Congratulations! You won!")
        break
        
        # Check if board is full
    if board_full(board):
        print("It's a tie!")
        break
        
        # AI's move
    print("AI is making a move...")
    ai_move(board)
    print_board(board)
        
        # Check if AI has won
    if check_win(board, "X"):
        print("AI wins! Better luck next time.")
        break
        
        # Check if board is full
    if board_full(board):
        print("It's a tie!")
        break

