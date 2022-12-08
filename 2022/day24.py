from functools import lru_cache
from itertools import product

from functions import *

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


file_path = INPUT_DIR + FILE_NAME
data = load_data(file_path)
blocks = []
block = []
for i in range(14):
    v1 = int(data[i * 18 + 4].split(" ")[-1])
    v2 = int(data[i * 18 + 5].split(" ")[-1])
    v3 = int(data[i * 18 + 15].split(" ")[-1])
    blocks.append([v1, v2, v3])


@lru_cache(maxsize=None)
def solve_z(w, z, v1, v2, v3):
    zs = []
    x = z - w - v3
    if x % 26 == 0:
        zs.append(x//26 * v1)
    if 0 <= w - v2 < 26:
        zs.append(w - v2 + z * v1)
    return zs
    

def alu(w_order):
    zs = {0}
    result = {}
    for (v1, v2, v3) in blocks[::-1]:
        new = set()
        for w, z in product(w_order, zs):
            possible_z = solve_z(w, z, v1, v2, v3)
            for pz in possible_z:
                new.add(pz)
                result[pz] = (w,) + result.get(z, ())
        zs = new
    return ''.join(str(d) for d in result[0])


def part1():
    return alu(range(1, 10))


def part2():
    return alu(range(1, 10)[::-1])


if __name__ == "__main__":
    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1()}")
    print(f"Answer to part 2 is {part2()}")
