import ast
import re
import math

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def add(str1, str2):
    return f'[{str1},{str2}]'


def reduce(line, once=False):
    i = 0
    while True:
        # print(line)
        i += 1
        exploded = False
        is_split = False

        ob = 0
        cb = 0
        for i, char in enumerate(line):
            if char == '[':
                ob += 1
                obi = i

            elif char == ']':
                cb += 1

            if (ob - cb) >= 4 and char == ']':
                exploded = True
                prev_nums = re.findall(r'\d+', line[:i])
                next_nums = re.findall(r'\d+', line[i:])

                sol = str(line[:obi])
                eol = str(line[i + 1:])
                if len(prev_nums) > 2:
                    l = str(int(prev_nums[-3]) + int(prev_nums[-2]))[::-1]
                    sol = sol[::-1].replace(prev_nums[-3][::-1], l, 1)[::-1]
                if next_nums:
                    r = str(int(prev_nums[-1]) + int(next_nums[0]))
                    eol = eol.replace(next_nums[0], r, 1)
                line = sol + '0' + eol
                if exploded:
                    break
        if once:
            print(line)
            return line

        if exploded:
            continue

        numbers = re.findall(r'\d\d+', line)
        if numbers:
            is_split = True
            line = line.replace(numbers[0], f'[{math.floor(int(numbers[0])/2)},{math.ceil(int(numbers[0])/2)}]', 1)
        if is_split:
            continue
        return line
    return line


def compute_number(_sum):
    def calc_number(pair):
        if isinstance(pair, list):
            return 3 * calc_number(pair[0]) + 2 * calc_number(pair[1])
        else:
            return pair
    return calc_number(ast.literal_eval(_sum))


def calc(data):
    current_sum = data[0]
    for line in data[1:]:
        current_sum = reduce(add(current_sum, line))
    return compute_number(current_sum)


def part1(data):
    return calc(data)


def part2(data):
    values = []

    for i, line1 in enumerate(data):
        for j, line2 in enumerate(data):
            if i != j:
                values.append(calc([line1, line2]))
    return max(values)


if __name__ == "__main__":
    # assert reduce('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
    # assert reduce('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
    # assert reduce('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
    # assert reduce('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    # stringy = add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')
    # reduce('[[[[12,12],[6,14]],[[0,[15,9]],[8,[8,1]]]],[2,9]]', True)
    # reduce('[[[[12,12],[6,14]],[[15,0],[17,[8,1]]]],[2,9]]', True)
    # assert reduce(reduce('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')) ==
    # reduce('[[[[0,6],[7,7]],[[[7,7],0],[7,8]]],[[10,[11,10]],[[0,8],[8,0]]]]')
    # reduce('[[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]],[2,9]]')
    # reduce('[[[[12,12],[6,14]],[[15,0],[17,[8,1]]]],[2,9]]', True)
    # print(reduce(add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')))
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3488, a2=3993)
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=4140, a2=3993)
    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
