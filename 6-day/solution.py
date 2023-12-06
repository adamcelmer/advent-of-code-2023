#!python
import re
import math
from decimal import *


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def parse_input(lines):
    times = [int(x) for x in re.findall(r'\d+', lines[0])]
    distances = [int(x) for x in re.findall(r'\d+', lines[1])]
    return times, distances


def solve_equation(max_time: int, distance_to_beat: int):
    # (7 - loading_time) * loading_time > distance
    # (7 - loading_time) * loading_time - distance > 0
    # 7 * loading_time - loading_time**2 - distance > 0
    # loading_time**2 - 7 * loading_time - distance > 0
    getcontext().prec = 50 # increase precision for sqrt
    delta = max_time ** 2 - 4 * distance_to_beat
    if delta <= 0:
        return []
    x1 = (- max_time - Decimal(delta).sqrt()) / -2
    x2 = (- max_time + Decimal(delta).sqrt()) / -2
    output = [x1, x2]
    output.sort()
    output[0] = math.ceil(output[0])
    output[1] = int(output[1])
    if distance_to_beat == (max_time - output[0]) * output[0]: # If our x1 or x2 is exactly the record, we have to exclude it
        output[0] = output[0] + 1
        output[1] = output[1] - 1
    return output


def part_1():
    times, distances = parse_input(read_lines())
    sum = 1
    for i in range(0, len(times)):
        max_time = times[i]
        distance_to_beat = distances[i]
        solution = solve_equation(max_time, distance_to_beat)
        if len(solution) == 2:
            sum *= len(range(solution[0], solution[1] + 1))
    print(f'Part 1: {sum}')


def part_2():
    times, distances = parse_input(read_lines())
    time_str = ""
    distance_str = ""
    for t in times:
        time_str += str(t)
    for d in distances:
        distance_str += str(d)
    solution = solve_equation(int(time_str), int(distance_str))
    print(f'Part 2: {len(range(solution[0], solution[1] + 1))}')


part_1()
part_2()
