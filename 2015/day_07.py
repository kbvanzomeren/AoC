from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def parse_data(data):
    values = {
        '1': 1,
        '2': 2
    }
    gates = []
    for line in data:
        _input, target = line.split(' -> ')
        if "NOT " in _input:
            gates.append(("NOT", _input.replace('NOT ', ""), "", target))
        elif ' ' in _input:
            for method in [" AND ", " OR ", " LSHIFT ", " RSHIFT "]:
                if method in _input:
                    x, y = _input.split(method)
                    gates.append((method.strip(), x, y, target))
        else:
            if _input.isdigit():
                values[target] = int(_input)
            else:
                gates.append(("INSERT", _input, "", target))
    return values, gates


def get_signal(values, gates):
    while "a" not in values and gates:
        skipped_gates = []
        for (gate, x, y, target) in gates:
            if x in values and gate in ["LSHIFT", "RSHIFT", "NOT", "INSERT"]:
                if gate == "LSHIFT":
                    values[target] = values[x] << int(y)
                elif gate == "RSHIFT":
                    values[target] = values[x] >> int(y)
                elif gate == "INSERT":
                    values[target] = values[x]
                elif gate == "NOT":
                    value = ''.join(['1' if b == '0' else '0' for b in '{0:016b}'.format(values[x])])
                    values[target] = int(value, 2)
            elif x in values and y in values and gate in ["AND", "OR"]:
                if gate == "AND":
                    values[target] = values[x] & values[y]
                elif gate == "OR":
                    values[target] = values[x] | values[y]
            else:
                skipped_gates.append((gate, x, y, target))
        gates = skipped_gates
    return values.get('a', 1)


def part1(data):
    values, gates = parse_data(data)
    return get_signal(values, gates)


def part2(data):
    value = part1(data)
    values, gates = parse_data(data)
    values['b'] = value
    return get_signal(values, gates)

if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
