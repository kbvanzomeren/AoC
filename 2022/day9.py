from functions.generic import *
from functions.load_data import load_data, load_data_split
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

MOVES = {"L": [-1, 0], "U": [0, 1], "R": [1, 0], "D": [0, -1]}


def prep_data(data):
    moves = []
    for m, d in data:
        moves.append([m, int(d)])
    return moves


def make_move_pro(_head, _tail):  # 🙈
    if abs(_head[0] - _tail[0]) == 2 or abs(_head[1] - _tail[1]) == 2:
        _tail[0] += (_head[0] - _tail[0]) // 2
        _tail[1] += (_head[1] - _tail[1]) // 2


def get_delta(val):
    return -1 if val < 0 else (1 if val > 0 else 0)


def make_move(_head, _tail):
    if abs(_head[0] - _tail[0]) == 2 or abs(_head[1] - _tail[1]) == 2:
        _tail[0] += get_delta(_head[0] - _tail[0])
        _tail[1] += get_delta(_head[1] - _tail[1])


def run_instructions(data, l_rope):
    moves = prep_data(data)
    rope = [[0, 0] for _ in range(l_rope)]
    visited = set()
    for move, distance in moves:
        for _ in range(distance):
            dx, dy = MOVES[move]
            rope[0][0] += dx
            rope[0][1] += dy
            for sub_head, sub_tail in zip(rope[:-1], rope[1:]):
                make_move(sub_head, sub_tail)
                # else:
                #     break
            visited.add(tuple(rope[-1]))
    return len(visited)


def part1(data):
    return run_instructions(data, 2)


def part2(data):
    return run_instructions(data, 10)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=88, a2=36, _load_data=load_data_split,
         _load_kwargs={"separator": ' '})

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split(file_path, ' ')
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
