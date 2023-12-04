from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def check_tickets(data):
    tickets = {}
    for card_id, line in enumerate(data):
        _, numbers = line.split(": ")
        winning, ticket = numbers.split(' | ')
        winning = [n for n in winning.split(' ')]

        matches = sum(n in winning for n in ticket.split(' ') if n != "")

        tickets[card_id + 1] = [matches, 1]
    return tickets


def part1(data):
    return sum([2 ** (ticket[0] - 1) if ticket[0] else 0 for _, ticket in check_tickets(data).items()])


def part2(data):
    tickets = check_tickets(data)
    for card_id, (matches, amount) in tickets.items():
        for extra_id in range(card_id + 1, card_id + 1 + matches):
            tickets[extra_id][1] += amount
    return sum(ticket[1] for _, ticket in tickets.items())


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
