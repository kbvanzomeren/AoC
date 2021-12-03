import itertools
from collections import defaultdict
from operator import add


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def get_neighbor_offsets(n_dimensions):
    neighbor_offsets = list(itertools.product([-1, 0, 1], repeat=n_dimensions))
    neighbor_offsets.remove((0,) * n_dimensions)
    return neighbor_offsets


def build_world(seq, n_dimensions):
    """Builds initial world from input."""
    extra_dims = [0] * (n_dimensions - 2)
    world = defaultdict(lambda: ".")
    for y, row in enumerate(seq):
        for x, val in enumerate(row):
            world[(x, y, *extra_dims)] = val
    return world


def count_active_neighbors(world, cube, offsets):
    """Count neighbors in world given cube coordinates."""
    active = 0
    for offset in offsets:
        neighbor = tuple(map(add, cube, offset))
        active += world[neighbor] == "#"
    return active


def simulate(world, cycles):
    """Simulate the world for multiple cycles"""
    # Ranges of cubes to consider
    ranges = list(map(lambda x: (min(x), max(x) + 1), zip(*world.keys())))
    n_dimensions = len(ranges)
    offsets = get_neighbor_offsets(n_dimensions)

    for cycle in range(1, cycles + 1):
        new_world = world.copy()
        for cube in itertools.product(*map(lambda r: range(r[0] - cycle, r[1] + cycle), ranges)):
            active = count_active_neighbors(world, cube, offsets)

            if world[cube] == "#" and active not in [2, 3]:
                new_world[cube] = "."
            elif world[cube] == "." and active == 3:
                new_world[cube] = "#"

        world = new_world
    return world


def test():
    data = load_data("test_input.txt")
    world = build_world(data, n_dimensions=3)
    world = simulate(world, 6)
    assert list(itertools.chain.from_iterable(world.values())).count("#") == 112

    # data = load_data("test_input.txt")
    world = build_world(data, n_dimensions=4)
    world = simulate(world, 6)
    assert list(itertools.chain.from_iterable(world.values())).count("#") == 848


if __name__ == "__main__":
    test()

    data = load_data('input.txt')
    world = build_world(data, n_dimensions=3)
    world = simulate(world, 6)
    print(list(itertools.chain.from_iterable(world.values())).count("#"))

    world = build_world(data, n_dimensions=4)
    world = simulate(world, 6)
    print(list(itertools.chain.from_iterable(world.values())).count("#"))