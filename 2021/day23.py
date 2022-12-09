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

to_int = {'.': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, '#': 9}
to_str = {v: k for k, v in to_int.items()}



class Point:
    def __init__(self, x, y, value, room=None):
        self.x = x
        self.y = y
        self.value = value
        self.neighbours = []
        self.room = room

    def is_amp(self):
        return 1 <= self.value <= 4

    def is_empty(self):
        return not self.value

    # def get_possible_coords(self):
    #     return []

    def allowed_stop(self, board):
        if not self.room:
            return self.x not in [3, 5, 7, 9]
        elif board.room_free(self.value):
            return True
        return False

    def can_move(self):
        return [_nb for _nb in self.neighbours if _nb.value == 0]

    def __str__(self):
        return f'{self.value} -> [{self.y}, {self.x}]'


# class Amphipod:
#     def __init__(self, value, point):
#         self.value = value
#         self.point = point
ALLOWED_ROOMS = {1: 3, 2: 5, 3: 7, 4: 9}

class Board:
    def __init__(self, _data):
        self._data = _data

        points = self.create_points()
        self.points = points
        self.free_points = []
        self.unlocked_rooms = []
        self.score = 0

    def is_room_free(self, amph):
        return False

    def create_points(self):
        points = []
        for y, row in enumerate(self._data):
            for x, val in enumerate(row):
                if val != '#':
                    room = None
                    if y != 1:
                        room = to_int[val]
                    points.append(Point(x=x, y=y, value=to_int[val], room=room))
        for point in points:
            nbs = []
            possible = [[point.y, point.x - 1], [point.y, point.x + 1], [point.y - 1, point.x], [point.y + 1, point.x]]
            for nb_point in points:
                if [nb_point.y, nb_point.x] in possible:
                    nbs.append(nb_point)
            point.neighbours = nbs
        return points

    def check_unlocked_rooms(self):

        for i in range(1, 5):
            if i not in self.unlocked_rooms:
                ind = ALLOWED_ROOMS[i]
                points = [point for point in self.points if point.y > 1 and point.x == ind]
                if all(p.value in [0, i] for p in points):
                    print(f'Room {i} is now unlocked')
                    self.unlocked_rooms.append(i)

    def print_points(self):
        for point in self.points:
            print(point)

    def print(self, _type='str'):

        for y, row in enumerate(self._data):
            _row = ''
            for x, v in enumerate(row):
                point = [p for p in self.points if p.y == y and p.x == x]
                if point:
                    if _type == 'str':
                        _row += to_str[point[0].value]
                    else:
                        _row += str(point[0].value)
                else:
                    _row += '#'
            print(_row)


    def get_free_points(self):
        self.free_points = []
        points2 = []
        for point in self.points:
            if point.y == 1 and point.x not in ALLOWED_ROOMS.values() or point.y != 1 and point.x in self.unlocked_rooms:
                self.free_points.append(point)
                points2.append(point.__str__())
        print(points2)

    # def get_valid_moves(self, point):
    #     for point in self.free_points:
    #         if po

    def check_possible_steps(self):
        apmh = []
        for point in self.points:
            if point.value:
                apmh.append(point.__str__())
        # for
        # print(apmh)

def part1(data):
    board = Board(data)
    board.check_unlocked_rooms()
    board.check_possible_steps()
    board.get_free_points()
    # print([[p.y, p.x] for p in points])
    # print(board.print_points())
    # board.print()
    board.print('int')
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")