import re
from functools import lru_cache

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    players = []
    for line in data:
        player, place = re.findall(r'\d+', line)
        players.append(int(place))
    return players


BOARD = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
M = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def part1(data):
    positions = prep_data(data)
    rolls = 2 * [i for i in range(1, 101)]
    roll_ind = 0
    real_roles = 0
    scores = [0, 0]
    while True:
        for player, position in enumerate(positions):
            total = sum(rolls[roll_ind: roll_ind + 3])
            real_roles += 3
            roll_ind = real_roles % 100

            positions[player] = BOARD[(position + total) % 10]
            scores[player] += positions[player]

            if scores[player] >= 1000:
                scores.pop(player)
                return scores[0] * real_roles


SCORE = 21

# ((9, 2), (15, 29), 0) -> 827322
@lru_cache(maxsize=None)
def play_game(_positions, _scores, player):
    wins = [0, 0]
    for total, m in M.items():
        positions = list(_positions)
        scores = list(_scores)
        positions[player] = BOARD[(positions[player] + total) % 10]
        scores[player] += positions[player]

        if scores[player] >= SCORE:
            wins[player] += m
        else:
            next_game = play_game(tuple(positions), tuple(scores), 0 if player else 1)
            wins[0] += next_game[0] * m
            wins[1] += next_game[1] * m
    return wins


def part2(data):
    positions = prep_data(data)
    return max(play_game(tuple(positions), (0, 0), 0))


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=739785, a2=444356092776315)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
