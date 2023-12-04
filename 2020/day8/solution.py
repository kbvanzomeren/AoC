import copy


def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    data = [[line.split(' ')[0], int(line.split(' ')[1])] for line in _data]
    return data


def game(data):
    position = 0
    acc_value = 0
    steps = 0
    visted_positions = []

    len_data = len(data)

    finished = False
    while position not in visted_positions and not finished:
        instruction, value = data[position]
        visted_positions.append(position)

        if instruction == 'acc':
            position += 1
            acc_value += value

        if instruction == 'jmp':
            position += value

        if instruction == 'nop':
            position += 1

        steps += 1
        if position == len_data:
            finished = True

    return steps, acc_value, finished


def part1(data):
    steps, acc_value, _ = game(data)
    return acc_value


def part2(data):
    for i, (inst, _) in enumerate(data):
        if inst != 'acc':
            _new_data = copy.deepcopy(data)
            _new_data[i][0] = 'nop' if inst == 'jmp' else 'jmp'

            steps, acc_value, finished = game(_new_data)

        if finished:
            break
    return acc_value


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 5
    assert part2(data) == 8


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
