import numpy as np

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


bounds = [-50, 50]


def prep_data(data):
    actions = []
    x, y, z = [], [], []
    cubes = []
    for line in data:
        elm = line.split('..')
        action = line[:2] == 'on'
        action2 = 1 if line[:2] == 'on' else 0
        x1 = int(elm[0].split('x=')[1])
        x2 = int(elm[1].split(',')[0])
        y1 = int(elm[1].split('y=')[1])
        y2 = int(elm[2].split(',')[0])
        z1 = int(elm[2].split('z=')[1])
        z2 = int(elm[3])

        x += [x1, x2]
        y += [y1, y2]
        z += [z1, z2]
        coords = [(x1, x2), (y1, y2), (z1, z2)]
        corners = [[x1, y1, z1], [x2, y2, z2]]
        actions.append([action, coords])
        cubes.append([action2, corners])
    return actions, cubes


LB = -50
UB = 51

def part1(data):
    on = set()
    actions, _ = prep_data(data)
    for a, [(x1, x2), (y1, y2), (z1, z2)] in actions:
        for x in range(max(LB, x1), min(UB, x2 + 1)):
            for y in range(max(LB, y1), min(UB, y2 + 1)):
                for z in range(max(LB, z1), min(UB, z2 + 1)):
                    if a:
                        on.add((x, y, z))
                    else:
                        on.discard((x, y, z))
    return len(on)


class Cube:
    def __init__(self, x, y, z, sign):
        self.x_min = x[0]
        self.x_max = x[1]
        self.y_min = y[0]
        self.y_max = y[1]
        self.z_min = z[0]
        self.z_max = z[1]
        self.sign = sign

    def size(self):
        return abs(self.x_max + 1 - self.x_min) * abs(self.y_max + 1 - self.y_min) * abs(self.z_max +1 - self.z_min) \
               * self.sign

    def has_overlap(self, cube2):
        # if cube2.x_max <= self.x_min or self.x_max <= cube2.x_min:
        if not(self.x_min <= cube2.x_max and self.x_max >= cube2.x_min):
            return False
        if not(self.y_min <= cube2.y_max and self.y_max >= cube2.y_min):
            return False
        if not(self.z_min <= cube2.z_max and self.z_max >= cube2.z_min):
            return False
        return True

    def get_overlap(self, cube2):
        x = [max(self.x_min, cube2.x_min), min(self.x_max, cube2.x_max)]
        y = [max(self.y_min, cube2.y_min), min(self.y_max, cube2.y_max)]
        z = [max(self.z_min, cube2.z_min), min(self.z_max, cube2.z_max)]

        sign = self.sign * cube2.sign

        if self.sign == cube2.sign:
            sign = -self.sign

        elif self.sign == 1 and cube2.sign == -1:
            sign = 1

        return Cube(x, y, z, sign)


def part2(data):
    actions, cubes = prep_data(data)
    all_cubes = []
    for a, (x, y, z) in actions:
        cc = Cube(x, y, z, a if a else -1)
        intersections = []
        for cube2 in all_cubes:
            if cc.has_overlap(cube2):
                intersections.append(cc.get_overlap(cube2))

        for _int in intersections:
            all_cubes.append(_int)

        if a == 1:
            all_cubes.append(cc)
    return sum([c.size() for c in all_cubes])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=474140, a2=2758514936282235)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
