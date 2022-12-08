def run(step):
    state = [0]
    len = 1
    position = 0
    for i in range(2017):
        ind = (position + step) % len + 1
        state.insert(ind, len)
        position = ind
        len += 1
        if not i % 500000:
            print(i)
    indy = state.index(2017)
    return state[indy + 1]


def run2(step):
    # After 0
    a0 = 1
    len = 1
    position = 0
    for i in range(50000000):
        ind = (position + step) % len + 1
        if ind == 1:
            a0 = len
        position = ind
        len += 1
        if not i % 500000:
            print(i)
    return a0


def run2b(step):
    from collections import deque

    puzzle = step
    spinlock = deque([0])

    for i in range(1, 50000001):
        spinlock.rotate(-puzzle)
        spinlock.append(i)

        if not i % 500000:
            print(i)
    return spinlock[spinlock.index(0) + 1]


def part1(step):
    return run(step)


def part2(step):
    return run2b(step)


def test() -> None:
    # data = load_data("test_input.txt")
    step = 3
    assert part1(step) == 638
    # assert part2(step) == 2


if __name__ == "__main__":
    test()

    # data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(382)}")
    print(f"Answer to part 2 is {part2(382)}")
