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
    def __init__(self):
        self.results = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.line = 0

    def run_code(self, data):
        print(self.results)
        print()
        while self.line < len(data):
            print(self.line, data[self.line])
            sleep(.2)
            dx = self.eval_line(data[self.line])
            self.line += dx
            print(self.line, self.results)
            print()

    def eval_line(self, line):
        return getattr(self, line[0])(line[1:])

    def cpy(self, _input):
        self.results[_input[1]] = int(_input[0])
        return 1

    def inc(self, _input):
        self.results[_input[0]] += 1
        return 1

    def dec(self, _input):
        self.results[_input[0]] -= 1
        return 1

    def jnz(self, _input):
        if self.results[_input[0]]:
            print(self.results[_input[0]])
            return int(_input[1])
        return 1


def part1(data):
    data = prep_data(data)
    ab = Assembunny()
    ab.run_code(data)
    return ab.results.get("a")


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=42, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
