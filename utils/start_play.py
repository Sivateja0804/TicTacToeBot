from utils.constants import *
from utils.parse_grid import *
from utils.input import *
from utils.print_statements import *
import time
import math


class game:
    def __init__(self):
        self.dp = {}

    def minmax(self, board, depth, isMax, tic_tac_toe_len):
        reward = calculate_reward(board, tic_tac_toe_len)

        if reward == 1000:
            return 1000 - depth
        if reward == -1000:
            return -1000 + depth

        if not check_legal_moves(board):
            return 0

        if isMax:
            bestVal = -math.inf
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == "_":
                        board[i][j] = player
                        key = convert_grid_to_string(board)
                        if (key, player) in self.dp:
                            reward = self.dp[(key, player)]
                        else:
                            reward = self.minmax(board, depth + 1, not isMax, tic_tac_toe_len)
                        if reward > bestVal:
                            bestVal = reward
                        self.dp[(key, player)] = reward
                        board[i][j] = "_"
            return bestVal
        else:
            bestVal = math.inf
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == "_":
                        board[i][j] = opponent
                        key = convert_grid_to_string(board)
                        if (key, opponent) in self.dp:
                            reward = self.dp[(key, opponent)]
                        else:
                            reward = self.minmax(board, depth + 1, not isMax, tic_tac_toe_len)
                        if reward < bestVal:
                            bestVal = reward
                        self.dp[(key, opponent)] = reward
                        board[i][j] = "_"
            return bestVal

    # calculate the optimal move of the bot
    def get_next_move(self, board, tic_tac_toe_len):
        bestReward = -math.inf
        bestMove = (-1, -1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "_":
                    board[i][j] = player
                    key = convert_grid_to_string(board)
                    if (key, player) in self.dp:
                        reward = self.dp[(key, player)]
                    else:
                        reward = self.minmax(board, 0, False, tic_tac_toe_len)
                    board[i][j] = "_"
                    if reward > bestReward:
                        bestReward = reward
                        bestMove = (i, j)

        return bestMove

    def start_game(self, grid, tic_tac_toe_len):
        while True:
            print_grids(grid)
            status = check_game_status(grid, tic_tac_toe_len)
            if status != "CONTINUE":
                break
            x, y = get_input_coordinates(grid)
            grid[x][y] = opponent
            print_grids(grid)
            status = check_game_status(grid, tic_tac_toe_len)
            time.sleep(1)
            if status == "CONTINUE":
                print("Now its my turn")
                startTime=time.time()
                optimalMove = self.get_next_move(grid, tic_tac_toe_len)
                grid[optimalMove[0]][optimalMove[1]] = player
                print("time taken for the move "+str(int(time.time()-startTime)))
            else:
                break
