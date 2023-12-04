from copy import deepcopy
from time import sleep

from functions.generic import *
from functions.load_data import load_data
import os
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


# def prep_data(data):
#     results = []
#     for line in data:
#         split_line = line.split(' ')
#         results.append(split_line)
#     return results

# class Duct:
#     def __init__(self, map):
#         self.map = map
#         self.postion

VALID_CHARS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0']


def get_moves(_map, current_position, x, y):
    moves = []
    # print(moves, _map, current_position, x, y)

    if 0 < current_position[0] - 1 and _map[current_position[0] - 1][current_position[1]] in VALID_CHARS:
        moves.append([current_position[0] - 1, current_position[1]])
    if current_position[0] < y + 1 and _map[current_position[0] + 1][current_position[1]] in VALID_CHARS:
        moves.append([current_position[0] + 1, current_position[1]])
    if 0 < current_position[1] - 1 and _map[current_position[0]][current_position[1] - 1] in VALID_CHARS:
        moves.append([current_position[0], current_position[1] - 1])
    if current_position[1] < x + 1 and _map[current_position[0]][current_position[1] + 1] in VALID_CHARS:

        moves.append([current_position[0], current_position[1] + 1])
    # print(moves)
    return moves


def find_start(_map, n):
    for i, row in enumerate(_map):
        for j, val in enumerate(row):
            if val == n:
                return [i, j]


def run_roomba(_map, x, y):
    cp = find_start(_map)
    paths = [{'cp': cp, 'vc': [cp], 'c': []}]
    step = 0
    while True:
        # sleep(1)
        new_paths = []
        step += 1
        # print(step)
        for path in paths:
            # print(path['cp'], path['vc'], path['c'])
            new_moves = get_moves(_map, path['cp'], x, y)
            for move in new_moves:
                if move not in path['vc']:
                    # print(move)
                    visited = list(path['vc'])
                    collected = list(path['c'])
                    visited.append(move)
                    if _map[move[0]][move[1]] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        if _map[move[0]][move[1]] not in collected:
                            collected.append(_map[move[0]][move[1]])
                            visited = [[move[0], move[1]]]
                            if len(collected) >= 4:
                                return step
                    new_paths.append({'cp': move, 'vc': visited, 'c':collected})
                    # print(new_paths)
        paths = new_paths


def run_roomba2(_map, x, y):
    collected = {}
    look_for = ['0', '1', '2', '3', '4', '5', '6', '7']
    for n in look_for:
        cp = find_start(_map, n)
        print(cp)
        collected[n] = {}
        visited = [cp]
        step = 1
        moves = get_moves(_map, cp, x, y)
        print_map(data, visited)
        while True:
            next_moves = []
            step += 1
            for move in moves:
                new_moves = get_moves(_map, move, x, y)
                # print(move, [m for m in new_moves if m not in visited])
                for new_move in new_moves:
                    if new_move not in visited:
                        visited.append(new_move)
                        next_moves.append(new_move)
                        # print(_map[new_move[0]][new_move[1]])
                        if _map[new_move[0]][new_move[1]] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if _map[new_move[0]][new_move[1]] not in collected[n]:
                                collected[n][_map[new_move[0]][new_move[1]]] = step
                            if len(collected[n]) == len(look_for) - 1:
                                break

            # sleep(1)
            # os.system('clear')
            # print_map(data, visited)

            moves = next_moves
            if not moves:
                break
    return collected

def get_shortest(collected, start='0'):
    collected_back = deepcopy(collected)
    for key, value in collected.items():
        if key != start:
            value.pop(start)

    paths = [[steps, key, [key]] for key, steps in collected[start].items()]
    count = 0
    while True:
        new_paths = []
        for path in paths:
            for key, value in collected[path[1]].items():
                if key not in path[2]:
                    v = list(path[2]) + [key]
                    new_paths.append([path[0] + value, key, v])
        paths = new_paths
        count += 1
        if count == 6:
            break
    for path in paths:
        path[0] += collected_back[path[1]]['0']
    return min([path[0] for path in paths])


def print_map(data, visited=[]):

    for i, row in enumerate(data):
        _row = ''
        for j, val in enumerate(row):
            if [i, j] in visited:
                _row += '0'
            else:
                _row += val
        print(_row)
    print(visited)


def part1(data):
    print_map(data)

    return 1

    x, y = len(data[0]), len(data)

    collected = run_roomba2(data, x, y)
    for key, value in collected.items():
        print(key, value)
    r = get_shortest(collected, '0')
    # print(collected)
    return r


def part2(data):
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=14, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
