initial_board = """
|o   o        o    |
| oo     o    oo o |
|    o  oo   oo    |
| oo               |
|   ooo      oo    |
|   o o      o     |
"""


def read_board(board):
    out = []
    for line in board.strip().splitlines():
        line = line.removeprefix('|').removesuffix('|')
        out.append(list(line))
    return out


def print_board(board):
    print('')
    for line in board:
        print('|' + ''.join(line) + '|')


def mutate_board(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            count = count_neighbors(board, x, y)
            if value_at(board, x, y) == 1:
                if count < 2:
                    board[y][x] = ' '
                elif count > 3:
                    board[y][x] = ' '
            elif count == 3:
                board[y][x] = 'o'


def count_neighbors(board, x, y):
    return value_at(board, x - 1, y - 1) + value_at(board, x, y - 1) + value_at(board, x + 1, y - 1) + value_at(board, x - 1, y) + \
        value_at(board, x + 1, y) + value_at(board, x - 1, y + 1) + \
        value_at(board, x, y + 1) + value_at(board, x + 1, y + 1)


def value_at(board, x, y):
    if board[y % len(board)][x % len(board[y % len(board)])] == 'o':
        return 1
    else:
        return 0


board = read_board(initial_board)
print_board(board)
while True:
    line = input('Press Enter to continue (q to quit)... ')
    if line == 'q':
        break
    mutate_board(board)
    print_board(board)
