def check_game_status(board=None):
    score = calculate_reward(board)
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


def calculate_reward(board):
    row_score = check_row_score(board)
    if row_score: return row_score

    column_score = check_column_score(board)
    if column_score: return column_score

    diagonal_score = check_diagonal_score(board)
    if diagonal_score: return diagonal_score

    return 0


def check_row_score(board, x=None, opponent=None, player=None):
    for i in range(len(board) - x + 1):
        if board[i:i + x] == [player] * x:
            return 1000
        if board[i:i + x] == [opponent] * x:
            return -1000
    return None


def check_column_score(board, x=None, player=None, opponent=None):
    for i in range(len(board) - x + 1):
        player_count = 0
        opponent_count = 0
        for j in range(x):
            if board[i + j][i] == player:
                player_count += 1
            elif board[i + j][i] == opponent:
                opponent_count += 1
        if player_count == x:
            return 1000
        if opponent_count == x:
            return -1000
    return None


# check all elements in the diagonal are equal if player won 10, lost -10
def check_diagonal_score(board, x, player=None, opponent=None):
    for i in range(len(board) - x + 1):
        player_count = 0
        opponent_count = 0
        for j in range(x):
            if board[i + x][i+x] == player:
                player_count += 1
            elif board[i + x][i+x] == opponent:
                opponent_count += 1
        if player_count == x:
            return 1000
        if opponent_count == x:
            return -1000

        player_count = 0
        opponent_count = 0
        for j in range(x):
            if board[i + x][len(board)-(i + x)-1] == player:
                player_count += 1
            elif board[i + x][len(board)-(i + x)-1] == opponent:
                opponent_count += 1
        if player_count == x:
            return 1000
        if opponent_count == x:
            return -1000
    return None


# check if there are legal moves(atleast one empty space)
def check_legal_moves(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "_":
                return True
    return False
