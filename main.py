from utils.start_play import *

if __name__ == "__main__":
    n = get_input_to_select_grid_len()
    grid = initialize_grid(n)
    tic_tac_toe_len = get_input_for_tic_tac_toe_len(n)
    g = game()
    g.start_game(grid, tic_tac_toe_len)
