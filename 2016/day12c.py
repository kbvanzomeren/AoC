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



def part1(data):

    instructions = prep_data(data)
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }

    def read(v):
        try:
            return int(v)
        except:
            return registers[v]

    ip = 0
    while True:
        if ip >= len(instructions):
            break
        ins = instructions[ip]

        sleep(0.3)
        print(ins)

        if ins[0] == 'cpy':
            registers[ins[2]] = read(ins[1])
        elif ins[0] == 'inc':
            registers[ins[1]] += 1
        elif ins[0] == 'dec':
            registers[ins[1]] -= 1
        elif ins[0] == 'jnz':
            if read(ins[1]) != 0:
                ip += read(ins[2])
                ip -= 1
        print(registers)
        ip += 1

    return registers['a']

def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=42, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
