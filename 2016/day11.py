from copy import deepcopy
from time import sleep

from functions import load_data
from functions.generic import *
from functions.test import test

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
    all_moves = []
    current_floor = floors[4 - elevator]
    possible_takes = []
    takes = list(current_floor)
    for i in current_floor:
        takes.remove(i)
        possible_takes.append([i])
        possible_takes += [[i, j] for j in takes]
    possible_floors = POSSIBLE_FLOORS[elevator]

    for pf in possible_floors:
        goes_up = pf > elevator
        floor_moves = []
        if pf in [1, 2] and not any(len(floors[4 - i]) for i in range(1, pf + 1)):
            continue
        for pt in possible_takes:
            if valid_moves(pt, current_floor, floors[4 - pf]):
                new_move = [pf, pt]
                if new_move not in last_move:
                    floor_moves.append([pf, pt])
        if goes_up and any(len(l[1]) == 2 for l in floor_moves):
            floor_moves = [m for m in floor_moves if len(m[1]) == 2]
        elif not goes_up and any(len(l[1]) == 1 for l in floor_moves):
            floor_moves = [m for m in floor_moves if len(m[1]) == 1]
        all_moves += floor_moves
    return all_moves


def map_rep(floors, elevator):
    stringy = f"E{elevator}-"
    i = 0
    for floor in floors:
        stringy += f"F{i}" + "".join(sorted(floor))
        i += 1
    return stringy


def run_simulation(floors, _resource_map, _resource_map_delta, elevator=1, n_items=4):
    stringy = map_rep(floors, elevator)
    visited = [stringy]
    map_reps = [
        {"floors": deepcopy(floors), "elevator": elevator, "last_move": []}
    ]
    steps = 0
    while True:
        steps += 1
        new_map_reps = []
        sleep(0.5)
        print(steps, len(map_reps))
        for _map_rep in map_reps:
            floors = _map_rep.get("floors")
            elevator = _map_rep.get("elevator")
            last_move = _map_rep.get("last_move")

            moves = find_moves(floors, elevator, last_move)
            for move in moves:
                f, pts = move
                new_floors = deepcopy(floors)
                for t in pts:
                    new_floors[4 - elevator].remove(t)
                    new_floors[4 - f].append(t)

                if len(new_floors[0]) == n_items:
                    return steps

                stringy = map_rep(new_floors, f)
                if stringy not in visited:
                    visited.append(stringy)
                    last_move = [[elevator, list(pts)]]
                    new_map_reps.append(
                        {"floors": deepcopy(new_floors), "elevator": f, "last_move": last_move}
                    )
        map_reps = deepcopy(new_map_reps)
    return steps


def part1(data):
    floors, _resource_map, _resource_map_delta = prep_data(data)
    steps = 0
    n_items = sum([len(_f) for _f in floors])
    print_layout(floors, _resource_map, _resource_map_delta, 1)
    steps = run_simulation(floors, _resource_map, _resource_map_delta, 1, n_items)
    return steps


def part2(data):
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=11, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
