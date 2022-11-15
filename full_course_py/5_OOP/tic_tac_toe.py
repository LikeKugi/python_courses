board = [' '] * 9


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for x, y, z in combinations:
        if state[x] == state[y] == state[z] and (state[x] == 'x' or state[x] == 'o'):
            return state[x]
    return False


def play_game(board):
    i = 1

    while not get_winner(board, winning_combinations):
        current_sign = ('x', 'o')[i > 0]
        index = int(input(f'index to put {current_sign} '))
        board[index] = current_sign

        print_state(board)

        winner_sign = get_winner(board, winning_combinations)
        if not winner_sign:
            print(f'winner is {current_sign}')

        i *= -1


play_game(board)