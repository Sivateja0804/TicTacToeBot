from utils.start_play import *
from utils.constants import *


def check_game_status(board=None, tic_tac_toe_len=None):
    score = calculate_reward(board, tic_tac_toe_len)
    if score == 1000:
        print("You Lost. Better Luck next time")
        return "GAME LOST"
    elif score == -1000:
        print("You Won")
        return "GAME WON"
    if not check_legal_moves(board):
        print("Game draw...")
        return "GAME DRAW"
    return "CONTINUE"


def calculate_reward(board, tic_tac_toe_len):
    row_score = check_row_score(board, x=tic_tac_toe_len)
    if row_score: return row_score

    column_score = check_column_score(board, x=tic_tac_toe_len)
    if column_score: return column_score

    diagonal_score = check_diagonal_score(board, x=tic_tac_toe_len)
    if diagonal_score: return diagonal_score

    return 0


def check_row_score(board, x=None):
    n = len(board)
    for row in board:
        for i in range(n - x + 1):
            if row[i:i + x] == [player] * x:
                return 1000
            if row[i:i + x] == [opponent] * x:
                return -1000
    return None


def check_column_score(board, x=None):
    for col in range(len(board)):
        for i in range(len(board) - x + 1):
            player_count = 0
            opponent_count = 0
            for j in range(x):
                if board[i + j][col] == player:
                    player_count += 1
                elif board[i + j][col] == opponent:
                    opponent_count += 1
            if player_count == x:
                return 1000
            if opponent_count == x:
                return -1000
    return None


# check all elements in the diagonal are equal if player won 10, lost -10
def check_diagonal_score(board, x):
    def check_count(board,i,j):
        legal_moves=[(1,-1),(1,1)]
        for m in range(2):
            player_count=0
            opponent_count=0
            for k in range(x):
                if 0<=i + (k*legal_moves[m][0])<len(board) and 0<=j + (k*legal_moves[m][1])<len(board):
                    if board[i + (k*legal_moves[m][0])][j + (k*legal_moves[m][1])] == player:
                        player_count += 1
                    elif board[i + (k*legal_moves[m][0])][j + (k*legal_moves[m][1])] == opponent:
                        opponent_count += 1
            if player_count == x:
                return 1000
            if opponent_count == x:
                return -1000
        return 0

    for i in range(len(board)):
        for j in range(len(board)):
            count=check_count(board,i,j)
            if count!=0:
                return count
    return None


# check if there are legal moves(atleast one empty space)
def check_legal_moves(board):
    n=len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == "_":
                return True
    return False


def convert_grid_to_string(board):
    key = ""
    n=len(board)
    for i in range(n):
        for j in range(n):
            key += board[i][j]
    return key
