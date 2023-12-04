#!python

class Card:
    def __init__(self, card_id: int, winning_numbers: [int], drawn_numbers: [int]):
        self.id = card_id
        self.winning_numbers = winning_numbers
        self.drawn_numbers = drawn_numbers

    def get_id(self):
        return self.id

    def get_matching_numbers(self):
        matching_numbers = []
        for num in self.drawn_numbers:
            if num in self.winning_numbers:
                matching_numbers.append(num)
        return matching_numbers


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def parse_input(lines: [str]) -> list[Card]:
    parsed_cards = []
    for line_index, line in enumerate(lines):
        winning_nums = line.split(" | ")[0].split(": ")[1].split()
        winning_nums = [int(x) for x in winning_nums]
        drawn_nums = line.split(" | ")[1].split()
        drawn_nums = [int(x) for x in drawn_nums]
        parsed_cards.append(Card(line_index + 1, winning_nums, drawn_nums))
    return parsed_cards


cards = parse_input(read_lines())


def part_1():
    sum = 0
    for card in cards:
        matching_nums = card.get_matching_numbers()
        if len(matching_nums) == 0:
            continue
        sum += 2**(len(matching_nums) - 1)
    print(f'Part 1: {sum}')


def part_2():
    card_count_map = {card.get_id(): 0 for card in cards}
    for card in cards:
        matching_nums = card.get_matching_numbers()
        card_count_map[card.get_id()] = card_count_map[card.get_id()] + 1
        for i in range(card.get_id() + 1, card.get_id() + 1 + len(matching_nums)):
            card_count_map[i] = card_count_map[i] + card_count_map[card.get_id()]
    total_count = sum(card_count_map.values())
    print(f'Part 2: {total_count}')


part_1()
part_2()
