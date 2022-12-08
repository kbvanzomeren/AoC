import inspect
from copy import deepcopy
from time import sleep

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

POSSIBLE_FLOORS = {
    1: [2],
    2: [3, 1],
    3: [4, 2],
    4: [3],
}


def print_layout(data, _resource_map, _resource_map_delta, elevator=1):
    _resource_map_inv = {val: key for key, val in _resource_map.items()}
    print("")
    for i, items in enumerate(data):
        floor = [f"F{4 - i}"] + [".."] * (len(_resource_map) * 2 + 1)
        if 4 - i == elevator:
            floor[1] = "E."
        for item in items:
            floor[_resource_map_delta[item]] = item
        print(floor)
    print("")


def prep_data(data):
    floors = []
    unique_items = []
    for i, line in enumerate(data):
        if "nothing relevant" in line:
            floors.append([])
        else:
            items = line.split('floor contains a ')[-1].replace('.', '').replace(', and a ', ',').replace(', a ', ',').replace(' and a ', ',').split(',')
            for item in items:
                if "generator" in item:
                    unique_items.append(item.replace('generator', ''))
            floors.append(items)
    _resource_map = {}
    _resource_map_delta = {}
    for i, res in enumerate(unique_items):
        _resource_map[res.strip()] = str(i)
        _resource_map_delta[str(i) + "G"] = i * 2 + 2
        _resource_map_delta[str(i) + "M"] = i * 2 + 3
    floors.reverse()
    for floor in floors:
        for i, spot in enumerate(floor):
            new_val = spot.replace('generator', 'G').replace('-compatible microchip', 'M').replace(' ', '')
            for key, val in _resource_map.items():
                new_val = new_val.replace(key, str(val))
            floor[i] = new_val
    return floors, _resource_map, _resource_map_delta


def valid_floor(floor, has_gen):
    for i in floor:
        if "M" in i and has_gen:
            _i = i.replace("M", "G")
            if _i not in floor:
                return False
    return True


def valid_moves(takes, _current_floor, _next_floor):
    current_floor = list(_current_floor)
    for take in takes:
        current_floor.remove(take)
    next_floor = _next_floor + takes
    for floor in [current_floor, next_floor]:
        has_gen = bool([i for i in floor if "G" in i])
        if not valid_floor(floor, has_gen):
            return False
    return True


def find_moves(floors, elevator, last_move):
    moves = []
    current_floor = floors[4 - elevator]
    possible_takes = []
    takes = list(current_floor)
    for i in current_floor:
        takes.remove(i)
        possible_takes.append([i])
        for j in takes:
            possible_takes.append([i, j])
    possible_floors = POSSIBLE_FLOORS[elevator]

    for pf in possible_floors:
        if pf in [1, 2] and not any(len(floors[4 - i]) for i in range(1, pf + 1)):
            continue
        for pt in possible_takes:
            if valid_moves(pt, current_floor, floors[4 - pf]):
                new_move = [pf, pt]
                if new_move not in last_move:
                    moves.append([pf, pt])
    return moves


def map_rep(floors, elevator):
    stringy = f"E{elevator}-"
    i = 0
    for floor in floors:
        stringy += f"F{i}" + "".join(sorted(floor))
        i += 1
    return stringy


def run_simulation(_floors, _resource_map, _resource_map_delta, elevator=1, last_move=[], memo={}, visited=[],
                   forced_moves=[]):
    floors = deepcopy(_floors)
    # print_layout(floors, _resource_map, _resource_map_delta, elevator)
    # visited = deepcopy(visited)
    stringy = map_rep(floors, elevator)
    # visited.append(stringy)
    # sleep(.5)
    # print_layout(floors, _resource_map, _resource_map_delta, elevator)
    #
    # if stringy in memo:
    #     return memo[stringy]
    #
    # if stringy in memo:
    #     memo[stringy] += 1
    #     if memo[stringy] > 2:
    #         memo[stringy] = None
    #         return None
    #
    # if len(floors[0]) == 8:
    #     memo[stringy] = []
    #     return []

    moves = find_moves(floors, elevator, last_move)
    if forced_moves:
        sleep(.3)
        print_layout(floors, _resource_map, _resource_map_delta, elevator)
        moves = [forced_moves[-1]]
        forced_moves = forced_moves[:-1]

    if not moves:
        memo[stringy] = None
        return None

    shortest_combination = None
    for move in moves:
        f, pts = move
        new_floors = deepcopy(floors)
        for t in pts:
            new_floors[4 - elevator].remove(t)
            new_floors[4 - f].append(t)

        _stringy = map_rep(new_floors, f)

        found_end = None
        # if _stringy not in memo:
        #     memo[_stringy] = 1
        last_move = [elevator, list(pts)]
        # last_move.append([elevator, list(pts)])
        # last_move = last_move[-3:]

        # if _stringy not in visited:
        found_end = run_simulation(new_floors, _resource_map, _resource_map_delta, f, last_move, memo, visited,
                                   forced_moves)
        if found_end is not None:
            # print_layout(floors, _resource_map, _resource_map_delta, elevator)
            combination = [*found_end, move]
            if shortest_combination is None or len(combination) <= len(shortest_combination):
                # print(combination)
                shortest_combination = combination
    memo[stringy] = shortest_combination
    return shortest_combination


def part1(data):
    floors, _resource_map, _resource_map_delta = prep_data(data)
    memo = {}
    fm = []
    # fm = [[4, ['1M', '1G']], [3, ['1M', '1G']], [2, ['1M', '1G']], [1, ['1G']], [2, ['1G']], [3, ['1G']], [4, ['0M', '0G']], [3, ['0M', '0G']], [2, ['0G']], [3, ['0G']], [4, ['1G', '0G']], [3, ['0G']], [2, ['0M']]]
    # fm = [[4, ['1M', '1G']], [3, ['1M', '1G']], [2, ['1M', '1G']], [1, ['1G']], [2, ['1G']], [3, ['1G']], [4, ['0M', '0G']], [3, ['0M', '0G']], [2, ['0G']], [3, ['0G']], [4, ['1G', '0G']], [3, ['1G', '0G']], [2, ['0M']]]
    # fm = [[4, ['1M', '1G']], [3, ['1M', '1G']], [2, ['1M', '1G']], [1, ['1G']], [2, ['1G']], [3, ['1G']], [4, ['0M', '0G']], [3, ['0G']], [4, ['1G', '0G']], [3, ['0M', '0G']], [2, ['0M']]]
    fm = [[4, ["0G", "0M"]], [3, ["0G", "0M"]], [2, ["0G", "0M"]], [1, ["0G"]], [2, ["0G"]], [3, ["0G"]], [4, ["1M", "1G"]], [3, ["1M", "1G"]], [2, ["1G"]], [3, ["1G"]], [4, ["0G", "1G"]], [3, ["1G"]], [4, ["2G", "2M"]], [3, ["0G"]], [4, ["0G", "1G"]], [3, ["1G"]], [4, ["3G", "3M"]], [3, ["0G"]], [4, ["0G", "1G"]], [3, ["0G", "1G"]], [2, ["0G", "1G"]], [1, ["1G"]], [2, ["1G"]], [3, ["1G"]], [4, ["4G", "4M"]], [3, ["2M", "3M"]],  [2, ["3M"]], [3, ["2G"]], [4, ["1G", "2G"]], [3, ["1G", "2G"]], [2, ["1G", "2G"]]]
    print(len(fm))
    test = run_simulation(floors, _resource_map, _resource_map_delta, 1, [], memo, visited=[], forced_moves=fm)
    # print_layout(floors, _resource_map, _resource_map_delta, fm[0][0])
    # print(test)

    print(len(memo[map_rep(floors, 1)]))
    print(memo[map_rep(floors, 1)])

    # for key, val in memo.items():
    #     print(key, val)
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)
    #
    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
