from functions.generic import *
from functions.load_data import load_data, load_data_split_empty
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


import re
REG = r'[-+]?\b\d+\b'


def prep_data(data):
    blueprints = []
    for line in data:
        blueprints.append([int(x) for x in re.findall(REG, line)])
    return blueprints


def clean_simulations(time, simulations, max_geod):

    if max_geod:
        return [s for s in simulations if (s[0][-1] + 1) * remainder + s[1][-1] >= max_geod]
    return simulations


def run_simulations(robots, resources, factory, blueprint, time=0, geos=0):
    _, ore_robot, clay_robot, obsidian_robot_ore, obsidian_robot_clay, geode_ore, geode_obsidian = blueprint
    _max_ore_cost = max([ore_robot, clay_robot, obsidian_robot_ore, geode_ore])
    _max_clay_cost = obsidian_robot_clay
    _max_obsidian_cost = geode_obsidian
    simulations = [[robots, resources]]
    old_max = max_geod = 0
    while time < 24:
        time += 1
        remainder = 24 - time
        print(f"== Minute {time} ==")
        new_simulations = []
        # sleep(1)

        for (robots, resources) in simulations:
            new_resources = [r + n for r, n in zip(resources, robots)]
            if new_resources[3] > max_geod:
                old_max = max_geod

                max_geod = new_resources[3]
            if time == 24 or not (robots[3] + 1) * remainder + resources[3] >= old_max:
                continue
            # new_robots = [0, 0, 0, 0]

            # print("----------")
            # print("Robots: ", robots)
            # print("Resour: ", resources)

            if resources[2] >= geode_obsidian and resources[0] >= geode_ore:
                    # print("Buying geode")
                    _resources = [new_resources[0] - geode_ore, new_resources[1], new_resources[2] - geode_obsidian, new_resources[3]]
                    new_robots = [robots[0], robots[1], robots[2], robots[3] + 1]
                    # print("Robots: ", new_robots)
                    # print("Resour: ", _resources)
                    new_simulations.append([new_robots, _resources])
            if resources[1] >= obsidian_robot_clay and resources[0] >= obsidian_robot_ore and robots[2] < _max_obsidian_cost:
                    # print("Buying Obsidian")
                    _resources = [new_resources[0] - obsidian_robot_ore, new_resources[1] - obsidian_robot_clay, new_resources[2], new_resources[3]]
                    new_robots = [robots[0], robots[1], robots[2] + 1, robots[3]]
                    # print("Robots: ", new_robots)
                    # print("Resour: ", _resources)
                    new_simulations.append([new_robots, _resources])
            if resources[0] >= clay_robot and robots[1] < _max_clay_cost:
                # print("Buying Clay")
                _resources = [new_resources[0] - clay_robot, new_resources[1], new_resources[2], new_resources[3]]
                new_robots = [robots[0], robots[1] + 1, robots[2], robots[3]]
                # print("Robots: ", new_robots)
                # print("Resour: ", _resources)
                new_simulations.append([new_robots, _resources])
            if resources[0] >= ore_robot and robots[0] < _max_ore_cost:
                # print("Buying Ora")
                _resources = [new_resources[0] - ore_robot, new_resources[1], new_resources[2], new_resources[3]]
                new_robots = [robots[0] + 1, robots[1], robots[2], robots[3]]
                # print("Robots: ", new_robots)
                # print("Resour: ", _resources)
                new_simulations.append([new_robots, _resources])

            # print("Saving")
            new_simulations.append([robots, new_resources])
            # print("Robots: ", robots)
            # print("Resour: ", new_resources)

        # print(len(new_simulations))
        simulations = clean_simulations(time, new_simulations, max_geod)
        # print(len(simulations))
        # print(max[x[1][-1]] for _, r, _, _,  in simulations)
    return max_geod




def part1(data):
    blueprints = prep_data(data)

    # Robots:  [1, 3, 0, 0]
    # Resour:  [2, 9, 0, 0]

    robots, resources, time = [1, 0, 0, 0], [0, 0, 0, 0], 0
    # robots, resources, time = [1, 3, 0, 0], [2, 9, 0, 0], 8
    # robots, resources, time = [1, 3, 0, 0], [3, 12, 0, 0], 9
    # robots, resources, time = [1, 3, 0, 0], [4, 15, 0, 0], 10
    # robots, resources, time = [1, 3, 1, 0], [2, 4, 0, 0], 11
    # robots, resources, time = [1, 4, 1, 0], [1, 7, 1, 0], 12
    #
    # robots, resources, time = [1, 4, 2, 0], [2, 9, 6, 0], 16
    # robots, resources, time = [1, 4, 2, 1], [2, 17, 3, 0], 18
    # robots, resources, time = [1, 4, 2, 2], [3, 29, 2, 3], 21
    # robots, resources, time = [1, 4, 1, 0], [1, 7, 1, 0], 13

    factory = [2, 9, 0, 0]
    total = 0
    for blueprint in blueprints:
        val = blueprint[0] * run_simulations(robots, resources, factory, blueprint, time=time, geos=0)
        total += val
        print(blueprint[0], val, total)
    return total


def part2(data):
    data = prep_data(data)
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=33, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
