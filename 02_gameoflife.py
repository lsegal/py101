import os

initial_board = """
|                                      |
|                         o            |
|                       o o            |
|             oo      oo            oo |
|            o   o    oo            oo |
| oo        o     o   oo               |
| oo        o   o oo    o o            |
|           o     o       o            |
|            o   o                     |
|             oo                       |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
"""

second_board = """"""


def read_board(board):
    out = []
    for line in board.strip().splitlines():
        line = line.removeprefix('|').removesuffix('|')
        row = []
        out.append(row)
        for c in list(line):
            if c == 'o':
                row.append(1)
            else:
                row.append(0)
    return out


def print_board(board, neighbor_count=False):
    os.system('clear')  # clear the screen (magic!)
    for row in range(len(board)):
        line = ''
        for col in range(len(board[row])):
            if board[row][col] == 1:
                if neighbor_count:
                    line += str(count_neighbors(board, row, col))
                else:
                    line += 'o'
            else:
                line += ' '
        print('|' + ''.join(line) + '|')


def evolve_board(board):
    new_board = []
    for row in range(len(board)):
        new_row = []
        new_board.append(new_row)
        for col in range(len(board[row])):
            neighbors = count_neighbors(board, row, col)
            value = board[row][col]
            if value == 1 and (neighbors < 2 or neighbors > 3):
                value = 0
            elif neighbors == 3:
                value = 1
            new_row.append(value)
    return new_board


def count_neighbors(board, row, col):
    count = 0
    for y in range(row - 1, row + 2):
        if y < 0 or y >= len(board):
            continue
        for x in range(col - 1, col + 2):
            if x < 0 or x >= len(board[y]):
                continue
            if x != col or y != row:
                count += board[y][x]
    return count


board = read_board(initial_board)
print_board(board)
while True:
    line = input('\nPress Enter to continue (q to quit)... ')
    if line == 'q':
        break
    board = evolve_board(board)
    print_board(board)
