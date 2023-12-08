#!python
import re
from math import lcm


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def parse_input(lines):
    instructions = ""
    nodes = {}
    for line in lines:
        if "=" in line:
            words = re.findall("[A-Z]+", line)
            nodes[words[0]] = (words[1], words[2])
        elif line:
            instructions = line
    return instructions, nodes


def part_1() -> int:
    instructions, nodes = parse_input(read_lines())
    current_node = "AAA"
    count = 1
    while True:
        for instruction in instructions:
            current_node = nodes[current_node][instruction == "R"]
            if current_node == "ZZZ":
                return count
            count += 1


def part_2() -> int:
    instructions, nodes = parse_input(read_lines())
    nodes_starting_with_a = list(filter(lambda x: x.strip()[-1] == 'A', list(nodes.keys())))
    count_per_node = []
    for node in nodes_starting_with_a:
        found = False
        count = 1
        while not found:
            for instruction in instructions:
                node = nodes[node][instruction == "R"]
                if node.endswith("Z"):
                    count_per_node.append(count)
                    found = True
                count += 1
    return lcm(*count_per_node)


print(part_1())
print(part_2())
