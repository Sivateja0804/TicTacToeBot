def get_input_to_select_grid_len():
    print("Please select the grid (NxN) len you want to play")
    try:
        n = input("Enter N from 3-12: ")
        if n < 3 or n > 12:
            print("Please enter the correct number ex: 4")
            return get_input_to_select_grid_len()
    except Exception:
        print("Please enter the correct number ex: 4")
        return get_input_to_select_grid_len()
    return n


def initialize_grid(n):
    grid = []
    for _ in range(n):
        grid.append(["_"] * n)
    return grid


def get_input_for_tic_tac_toe_len(n):
    print("Enter the tic tac toe length")
    try:
        x = input("Enter x:")
        if x < 3 or x > n:
            print("Please enter the correct number ex: 3")
            return get_input_for_tic_tac_toe_len(n)
    except Exception:
        print("Please enter the correct number ex: 3")
        return get_input_for_tic_tac_toe_len()
    return x

