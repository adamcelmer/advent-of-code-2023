#!python
from collections import Counter

card_labels_p1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_labels_p2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
hand_types = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


class Hand:
    def __init__(self, cards, bid, is_part2=False):
        self.is_part2 = is_part2
        self.cards = cards
        self.bid = bid
        self.type = self.determine_type()

    def __repr__(self) -> str:
        return f'{self.cards} | {self.type} | {self.bid}'

    def __eq__(self, other) -> bool:
        return self.cards == other.cards

    def __lt__(self, other) -> bool:
        if hand_types.index(self.type) > hand_types.index(other.type):
            return False
        elif hand_types.index(self.type) < hand_types.index(other.type):
            return True
        else:
            for i in range(0, len(self.cards)):
                card_labels = card_labels_p2 if self.is_part2 else card_labels_p1
                if card_labels.index(self.cards[i]) > card_labels.index(other.cards[i]):
                    return False
                elif card_labels.index(self.cards[i]) < card_labels.index(other.cards[i]):
                    return True
        return False

    def __gt__(self, other) -> bool:
        card_labels = card_labels_p2 if self.is_part2 else card_labels_p1
        if hand_types.index(self.type) > hand_types.index(other.type):
            return True
        elif hand_types.index(self.type) < hand_types.index(other.type):
            return False
        else:
            for i in range(0, len(self.cards)):
                if card_labels.index(self.cards[i]) > card_labels.index(other.cards[i]):
                    return True
                elif card_labels.index(self.cards[i]) < card_labels.index(other.cards[i]):
                    return False
        return False

    def determine_type(self) -> str:
        cards = self.replace_jokers(self.cards) if self.is_part2 else self.cards
        cards_counter = Counter(cards)
        if len(cards_counter.keys()) == 1:
            return "Five of a kind"
        if 4 in cards_counter.values():
            return "Four of a kind"
        if 3 in cards_counter.values() and 2 in cards_counter.values():
            return "Full house"
        if 3 in cards_counter.values():
            return "Three of a kind"
        if len([key for key, value in cards_counter.items() if value == 2]) == 2:
            return "Two pair"
        if len([key for key, value in cards_counter.items() if value == 2]) == 1:
            return "One pair"
        return "High card"

    @staticmethod
    def replace_jokers(cards):
        cards_counter = Counter(cards)
        most_common_card = cards_counter.most_common()[0][0]
        if most_common_card == "J" and cards != ["J", "J", "J", "J", "J"]:
            most_common_card = cards_counter.most_common()[1][0]
        return [most_common_card if x == "J" else x for x in cards]


def part_1(lines: list[str]):
    hands = []
    for line in lines:
        cards = [x for x in line.split(" ")[0]]
        bid = int(line.split(" ")[1])
        hands.append(Hand(cards, bid))
    sum = 0
    hands.sort()
    for index, hand in enumerate(hands, start=1):
        sum += index * hand.bid
    print(f'Part 1: {sum}')


def part_2(lines: list[str]):
    hands = []
    for line in lines:
        cards = [x for x in line.split(" ")[0]]
        bid = int(line.split(" ")[1])
        hands.append(Hand(cards, bid, is_part2=True))
    sum = 0
    hands.sort()
    for index, hand in enumerate(hands, start=1):
        sum += index * hand.bid
    print(f'Part 2: {sum}')


lines = read_lines()
part_1(lines)
part_2(lines)
