from utils.print_statements import *
from utils.parse_grid import *


def start_game(grid):
    while True:
        print_grids(grid)
        status = check_game_status(grid)
        # if status != "CONTINUE":
        #     break
        # print("Its your Turn Make a move : select 00-22 ex 00 01 02 10 11 12 20 21 22")
        # x, y = get_input()
        # if board[x][y] != "_":
        #     print("please select an empty place")
        #     continue
        # else:
        #     board[x][y] = opponent
        #     print_board(board)
        #     status = check_game_status(board)
        #     time.sleep(1)
        #     if status == "CONTINUE":
        #         print("Now its my turn")
        #         optimalMove = get_next_move(board)
        #         board[optimalMove[0]][optimalMove[1]] = player
        #     else:
        #         break
