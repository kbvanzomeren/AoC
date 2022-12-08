from time import sleep

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    results = []
    for line in data:
        split_line = line.split(' ')
        results.append(split_line)
    return results


class Assembunny:
    def __init__(self, a):
        self.results = {"a": a, "b": 0, "c": 0, "d": 0}
        self.line = 0
        self.prev_out = 1

    def run_code(self, data):
        while self.line < len(data):
            # print(self.line, data[self.line])
            # sleep(.2)
            dx = self.eval_line(data[self.line])
            self.line += dx
            # print(self.line, self.results)
            # print()

    def get_value(self, _val):
        try:
            val = int(_val)
        except ValueError:
            val = self.results[_val]
        return val

    def eval_line(self, line):
        return getattr(self, line[0])(line[1:])

    def cpy(self, _input):
        self.results[_input[1]] = self.get_value(_input[0])
        return 1

    def inc(self, _input):
        self.results[_input[0]] += 1
        return 1

    def dec(self, _input):
        self.results[_input[0]] -= 1
        return 1

    def jnz(self, _input):
        if self.get_value(_input[0]):
            return int(_input[1])
        return 1

    def out(self, _input):
        if self.get_value(_input[0]) == self.prev_out:
            return 50
        else:
            self.prev_out = self.get_value(_input[0])
        return 1


def part1(data):
    data = prep_data(data)
    i = 0
    while True:
        print(i)
        ab = Assembunny(i)
        ab.run_code(data)
        i += 1
    return ab.results.get("a")


def part2(data):
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=42, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
