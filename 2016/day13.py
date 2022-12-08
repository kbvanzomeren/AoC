from copy import deepcopy
from time import sleep
import os


from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')
SIZE = 50
OD = 1364


def print_maze(maze, moves=[]):
    for y, row in enumerate(maze):
        line = ''
        for x, val in enumerate(row):
            if val:
                line += "#"
            elif [y - 1, x] in moves:
                line += "0"
            else:
                line += "."
        print(line)


def prep_data():
    maze = []
    for y in range(SIZE):
        row = []
        for x in range(SIZE):
            _b = "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + OD)
            p = 1 if _b.count('1') % 2 else 0
            row.append(p)
        maze.append(row)
    return maze


def possible_moves(current, maze, visited):
    moves = []
    inbound = []
    if current[0] - 1 >= 0:
        inbound.append([current[0] - 1, current[1]])
    if current[0] + 1 < SIZE:
        inbound.append([current[0] + 1, current[1]])
    if current[1] - 1 >= 0:
        inbound.append([current[0], current[1] - 1])
    if current[1] + 1 < SIZE:
        inbound.append([current[0], current[1] + 1])
    for ny, nx in inbound:
        if not maze[ny][nx] and [ny, nx] not in visited:
            moves.append([ny, nx])
    return moves


def part1(data):
    current_steps = 0
    maze = prep_data()
    current = [1, 1]
    visited = [[1, 1]]
    new_moves = possible_moves(current, maze, visited)

    while True:
        moves = deepcopy(new_moves)
        new_moves = []
        # sleep(0.3)
        # os.system('clear')
        # print_maze(maze, moves)
        if not moves:
            print("No more moves")
            break
        for y, x in moves:
            if [y, x] not in visited:
                visited.append([y, x])
                new_moves += possible_moves([y, x], maze, visited)
        current_steps += 1
        if current_steps == 50:
            print(len(visited))
            break

        if [39, 31] in visited:
            break
    return current_steps


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=11, a2=2)

    # file_path = INPUT_DIR + FILE_NAME
    # data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
