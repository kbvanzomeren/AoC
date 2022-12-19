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


def run_simulations(robots, resources, blueprint, max_time=24):
    cost_ore_robot, cost_clay_robot, cost_obsidian_robot_ore, cost_obsidian_robot_clay, cost_geode_ore, cost_geode_obsidian = blueprint
    _max_ore_cost = max([cost_ore_robot, cost_clay_robot, cost_obsidian_robot_ore, cost_geode_ore])
    simulations = [(robots, resources)]
    max_geode = n_max_geode = 0
    for _time in range(max_time):
        new_simulations = set()
        remainder = max_time - 1 - _time

        for (rob_ore, rob_clay, rob_obs, rob_geo), (ore, clay, obs, geo) in simulations:
            _ore = ore + rob_ore
            _clay = clay + rob_clay
            _obs = obs + rob_obs
            _geo = geo + rob_geo
            if _geo > max_geode:
                max_geode = _geo
                n_max_geode = rob_geo

            new_simulations.add(((rob_ore, rob_clay, rob_obs, rob_geo), (_ore, _clay, _obs, _geo)))
            if ore >= cost_ore_robot and rob_ore <= _max_ore_cost:
                new_simulations.add(((rob_ore + 1, rob_clay, rob_obs, rob_geo), (_ore - cost_ore_robot, _clay, _obs,
                                                                                 _geo)))
            if ore >= cost_clay_robot and rob_clay <= cost_obsidian_robot_clay:
                new_simulations.add(((rob_ore, rob_clay + 1, rob_obs, rob_geo), (_ore - cost_clay_robot, _clay, _obs,
                                                                                 _geo)))
            if ore >= cost_obsidian_robot_ore and clay >= cost_obsidian_robot_clay and rob_obs <= cost_geode_obsidian:
                new_simulations.add(((rob_ore, rob_clay, rob_obs + 1, rob_geo), (_ore - cost_obsidian_robot_ore,
                                                                                 _clay - cost_obsidian_robot_clay, _obs,
                                                                                 _geo)))
            if ore >= cost_geode_ore and obs >= cost_geode_obsidian:
                new_simulations.add(((rob_ore, rob_clay, rob_obs, rob_geo + 1), (_ore - cost_geode_ore, _clay,
                                                                                 _obs - cost_geode_obsidian,
                                                                                 _geo)))

        simulations = set(s for s in new_simulations if s[1][3] + (s[0][3] + 1) * remainder >= max_geode + n_max_geode * remainder)
    return max_geode


def part1(data):
    blueprints = prep_data(data)
    robots, resources, max_time = (1, 0, 0, 0), (0, 0, 0, 0), 24

    total = 0
    for blueprint in blueprints:
        val = blueprint[0] * run_simulations(robots, resources, blueprint[1:], max_time=max_time)
        total += val
    return total


def part2(data):
    blueprints = prep_data(data)
    robots, resources, max_time = (1, 0, 0, 0), (0, 0, 0, 0), 32
    total = 1
    for blueprint in blueprints[:3]:
        val = run_simulations(robots, resources, blueprint[1:], max_time=max_time)
        total *= val
    return total


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=33, a2=56 * 62)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
