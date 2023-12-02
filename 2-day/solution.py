#!python

max_red = 12
max_green = 13
max_blue = 14


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def parse_set(set_raw: str) -> {}:
    return {x.split(" ")[1]: int(x.split(" ")[0]) for x in set_raw.split(", ")}


def part_1(lines):
    sum = 0
    id = 1
    for line in lines:
        is_possible = True
        sets_raw = line.split(": ")[1].split("; ")
        sets = [parse_set(set_raw) for set_raw in sets_raw]
        for set in sets:
            if ('red' in set and set['red'] > max_red) or ('green' in set and set['green'] > max_green) or ('blue' in set and set['blue'] > max_blue):
                is_possible = False
        if is_possible:
            sum += id
        id += 1
    print(sum)


def part_2(lines):
    sum = 0
    for line in lines:
        sets_raw = line.split(": ")[1].split("; ")
        sets = [parse_set(set_raw) for set_raw in sets_raw]
        min_red = 0
        min_green = 0
        min_blue = 0
        for set in sets:
            if 'red' in set and set['red'] > min_red:
                min_red = set['red']
            if 'green' in set and set['green'] > min_green:
                min_green = set['green']
            if 'blue' in set and set['blue'] > min_blue:
                min_blue = set['blue']
        sum += min_red * min_green * min_blue
    print(sum)

lines = read_lines()
part_1(lines)
part_2(lines)
