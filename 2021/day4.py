# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    rounds = data[0].split(',')
    cards = []
    cards_flatten = []
    card = []
    for row in data[2:]:
        if not row:
            cards.append(card)
            cards_flatten.append([n for row in card for n in row])
            card = []
        else:
            card.append([i for i in row.split(' ') if i])

    cards.append(card)
    cards_flatten.append([n for row in card for n in row])
    shadow_cards = [[[0] * 5 for _ in range(5)] for _ in range(len(cards))]
    return rounds, cards, shadow_cards, cards_flatten


def check_card(card, shadow_card, flatten_card, ignore_cards=[]):
    win = False
    for row in shadow_card:
        if sum(row) == 5:
            # row_i = i
            win = True

    for i in range(5):
        _sum = sum([row[i] for row in shadow_card])
        if _sum == 5:
            win = True

    _sum = 0
    if win:
        ignore_cards.append(flatten_card)
        for row, shadow_row in zip(card, shadow_card):
            for i, si in zip(row, shadow_row):
                if not si:
                    _sum += int(i)
    return _sum


def cross_number(card, shadow_card, number):
    for i, row in enumerate(card):
        if number in row:
            for j, value in enumerate(row):
                if value == number:
                    shadow_card[i][j] = 1
                    return


def part1(data):
    rounds, cards, shadow_cards, cards_flatten = prep_data(data)
    for round in rounds:
        print('-- NUMBER --', round)
        for card, shadow_card, flatten_card in zip(cards, shadow_cards, cards_flatten):
            # for i in range(5):
            #     print(card[i])
            if round in flatten_card:
                cross_number(card, shadow_card, round)
                win = check_card(card, shadow_card, flatten_card)
                if win:
                    return win * int(round)
    return 1


def part2(data):
    rounds, cards, shadow_cards, cards_flatten = prep_data(data)

    ignore_cards = []
    for round in rounds:
        for card, shadow_card, flatten_card in zip(cards, shadow_cards, cards_flatten):
            if round in flatten_card and flatten_card not in ignore_cards:
                cross_number(card, shadow_card, round)

                win = check_card(card, shadow_card, flatten_card, ignore_cards=ignore_cards)

                if len(ignore_cards) == len(cards):
                    return win * int(round)

    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=4512, a2=1924)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
