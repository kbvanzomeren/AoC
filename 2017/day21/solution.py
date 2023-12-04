from copy import copy


def get_string_rep(_matrix):
    return ''.join(''.join(row) for row in _matrix)


def flip(_matrix, axis):
    if axis == 'x':
        return [row[::-1] for row in _matrix]
    if axis == 'y':
        return _matrix[::-1]


def rotate(_matrix):
    return list(zip(*_matrix[::-1]))


def add_rule(_in, _out, playbook):
    _id = get_string_rep(_in)
    playbook[_id] = copy(_out)


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    rules = []
    for line in data:
        _input, _output = line.split(' => ')
        _input_array = [[sym for sym in row] for row in _input.split('/')]
        _output_array = [[sym for sym in row] for row in _output.split('/')]
        rules.append([_input_array, _output_array])
    playbook = {}
    for _in, _out in rules:
        # Normal rotations
        current_in = copy(_in)
        for _ in range(4):
            add_rule(current_in, _out, playbook)
            current_in = rotate(current_in)

        # Flip x rotations
        current_in = copy(_in)
        current_in = flip(current_in, 'x')
        for _ in range(4):
            add_rule(current_in, _out, playbook)
            current_in = rotate(current_in)

        # Flip x rotations
        current_in = copy(_in)
        current_in = flip(current_in, 'y')
        for _ in range(4):
            add_rule(current_in, _out, playbook)
            current_in = rotate(current_in)
    return playbook

INITIAL = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"],
]


def merge_pattern(patterns):
    new_pattern = []
    for pattern_row in patterns:
        for i in range(len(pattern_row[0][0])):
            new_line = []
            for pattern in pattern_row:
                new_line += pattern[i]
            new_pattern.append(new_line)

    return new_pattern


def run_program(pattern, playbook, rounds):
    for i in range(rounds):
        len_pattern = len(pattern)
        size = 2 + len_pattern % 2
        n_patterns = len_pattern//size

        patterns = [list() for _ in range(n_patterns)]
        for ri in range(n_patterns):
            pattern_row = []
            for ci in range(n_patterns):
                sub_pattern = [_row[ci * size: (ci + 1) * size] for _row in pattern[ri * size: (ri + 1) * size]]
                # print(sub_pattern, ' => ', playbook[get_string_rep(sub_pattern)])
                pattern_row.append(playbook[get_string_rep(sub_pattern)])
            patterns[ri] += pattern_row
        pattern = merge_pattern(patterns)

    count = 0
    for _row in pattern:
        count += _row.count('#')
    return count


def part1(playbook, rounds):
    return run_program(INITIAL, playbook, rounds)


def part2(playbook, rounds):
    return run_program(INITIAL, playbook, rounds)


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data, 2) == 12
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data, 5)}")
    print(f"Answer to part 2 is {part2(data, 18)}")
