#!python

def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def parse_input(lines: []) -> ([], {}):
    numbers = []    # [{123: [(1,2), (1,3)]}]
    symbols = {}    # {(1,2): '$'}
    for line_index, line in enumerate(lines):
        num_str = ""
        num_coords = []
        for char_index, char in enumerate(line):
            if char.isdigit():
                num_str += char
                num_coords.append((line_index, char_index))
            if (not char.isdigit() or char_index == len(line) - 1) and len(num_str) > 0:
                numbers.append((int(num_str), num_coords))
                num_str = ""
                num_coords = []
            if not char.isdigit() and char != '.':
                symbols[(line_index, char_index)] = char
    return numbers, symbols


def get_coord_neighbours(line_idx, col_idx):
    return [(line_idx + 1, col_idx - 1), (line_idx + 1, col_idx), (line_idx + 1, col_idx + 1),
            (line_idx, col_idx - 1), (line_idx, col_idx + 1),
            (line_idx - 1, col_idx - 1), (line_idx - 1, col_idx), (line_idx - 1, col_idx + 1)]


def is_adjacent(coord: tuple):
    line_idx, col_idx = coord
    neighbours = get_coord_neighbours(line_idx, col_idx)
    for key in symbols.keys():
        if key in neighbours:
            return True
    return False


numbers, symbols = parse_input(read_lines())


def part_1():
    sum = 0
    for number, coords in numbers:
        for coord in coords:
            if is_adjacent(coord):
                sum += number
                break
    print(sum)


def part_2():
    stars = [k for k, v in symbols.items() if v == '*']
    coord_num_map = {}
    for num, coords in numbers:
        for coord in coords:
            coord_num_map[coord] = num
    sum = 0
    for line_idx, col_idx in stars:
        adjacent_numbers = set()
        star_neighbours = get_coord_neighbours(line_idx, col_idx)
        for neighbour in star_neighbours:
            if neighbour in coord_num_map:
                adjacent_numbers.add(coord_num_map[neighbour])
        if len(adjacent_numbers) == 2:
            sum += list(adjacent_numbers)[0] * list(adjacent_numbers)[1]
    print(sum)


part_1()
part_2()
