#!python
import re


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def get_diffs(nums: list[int]) -> list[int]:
    diffs = []
    for i in range(1, len(nums)):
        diffs.append(nums[i] - nums[i - 1])
    return diffs


def get_all_diffs(nums: list[int]) -> list[list[int]]:
    diffs = [get_diffs(nums)]
    while len([x for x in diffs[-1] if x != 0]) > 0:
        diffs.append(get_diffs(diffs[-1]))
    return diffs


def find_last_value(nums: list[int]) -> int:
    diffs = get_all_diffs(nums)
    for i in range(len(diffs) - 1, 0, -1):
        diffs[i - 1].append(diffs[i][-1] + diffs[i - 1][-1])
    return nums[-1] + diffs[0][-1]


def find_first_value(nums: list[int]) -> int:
    diffs = get_all_diffs(nums)
    diffs[-1].append(0)
    for i in range(len(diffs) - 1, 0, -1):
        diffs[i - 1].insert(0, diffs[i - 1][0] - diffs[i][0])
    return nums[0] - diffs[0][0]


def part_1() -> int:
    histories = [[int(number) for number in history] for history in
                 [re.findall("[-]?[\d]+", line) for line in read_lines()]]
    sum = 0
    for history in histories:
        sum += find_last_value(history)
    return sum


def part_2() -> int:
    histories = [[int(number) for number in history] for history in
                 [re.findall("[-]?[\d]+", line) for line in read_lines()]]
    sum = 0
    for history in histories:
        sum += find_first_value(history)
    return sum


print(part_1())
print(part_2())
