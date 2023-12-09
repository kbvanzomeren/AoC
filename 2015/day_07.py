from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

_map = {**{str(n): n for n in range(1, 10)}, **{'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}}


def order(hands, part):
    strength_order = defaultdict(list)
    for cards in hands.keys():
        if part == 1:
            jokers = 0
            counter = {c: cards.count(c) for c in cards}
        else:
            _map['J'] == 1
            counter = {c: cards.count(c) for c in cards if c != "J"}
            jokers = cards.count("J")
        if jokers == 5 or len(counter) == 1:
            strength = 21
        elif max(counter.values()) + jokers == 4:
            strength = 20
        elif max(counter.values()) + jokers == 3:
            strength = 18
            if jokers <= 1 and min(counter.values()) == 2:
                strength = 19
        elif max(counter.values()) + jokers == 2:
            strength = 16
            if jokers == 0 and len(counter) == 3:
                strength = 17
        else:
            # Don't need to order high cards ... 🤕
            # _type = max([_map[c] for c in cards])
            strength = 1
        strength_order[strength].append(cards)

    final_strength_order = []
    for score in range(21, 0, -1):
        final_strength_order += check_tiebreaker(strength_order.get(score, []), 0)
        
    return final_strength_order


def check_tiebreaker(games, i):
    new_order = []
    initial_shuffel = defaultdict(list)
    for game in games:
        initial_shuffel[_map[game[i]]].append(game)

    for ci in range(14, 0, -1):
        games_to_order = initial_shuffel.get(ci, [])
        if len(initial_shuffel.get(ci, [])) > 1:
            new_order += check_tiebreaker(games_to_order, i + 1)
        else:
            new_order += games_to_order
    return new_order


def read_hands(data):
    scores = {}
    for line in data:
        cards, bid = line.split(' ')
        scores[cards] = int(bid)
    return scores


def score_games(final_order, scores):
    final = 0
    _max = len(final_order)
    for cards in final_order:
        final += _max * scores[cards]
        _max -= 1
    return final


def part1(data):
    hands = read_hands(data)
    new_order = order(hands, part=1)
    return score_games(new_order, hands)


def part2(data):
    hands = read_hands(data)
    new_order = order(hands, part=2)
    return score_games(new_order, hands)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
