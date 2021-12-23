from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


_map = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 9, 9, 4, 9, 1, 9, 3, 9, 4, 9, 9, 9],
    [9, 9, 9, 2, 9, 3, 9, 2, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

cost = {
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}

allowed_room = {
    1: 3,
    2: 5,
    3: 7,
    4: 9
}

class Point:
    def __init__(self, x, y, is_wall):
        self.x = x
        self.y = y
        self.is_wall = is_wall
        self.contains_amp = False
        self.is_locked = False
        self.can_stop = False

    def check_locked_status(self):
        if self.is_wall or not self.is_locked:
            return
        if 1 < self.y <= 5 and x % :


    def __str__(self):
        if self.is_wall:
            return '#'



class Amphipod:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def can_stop(self):
        return self.y != 1 or self.x not in allowed_room.values()

    def get_possible_coords(self):



def get_neighbours(_map, x, y, amp):

    coords = []
    for (yi, xi) in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
        if _map[yi][xi] == 0:
            allowed_room_ind = allowed_room[amp]

            coords.append([xi, yi])

    return [[yi, xi]



def run_round(_map, energy):
    pass

def part1(data):
    for y in range(1, 4):
        for x in range(1, 12):
            amp = _map[y][x]
            if _map[y][x] != 9 and _map[y][x] != 0:
                nbs = get_neighbours(_map, x, y)
                if nbs:
                    print(amp)
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")