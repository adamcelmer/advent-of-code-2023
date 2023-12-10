#!python


def read_lines() -> [str]:
    with open('input.txt') as file:
        return file.read().splitlines()


def find_s(map: list[list[str]]) -> tuple[int, int]:
    for row_idx, row in enumerate(map):
        if "S" in row:
            return row_idx, row.index("S")


def find_surrounding_pipes(row, col, max_rows, max_cols):
    return [(x, y) for x, y in [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
            if 0 <= x < max_rows and 0 <= y < max_cols]


def pipes_match(pipes_map: list[list[str]], pipe_1: tuple[int, int], pipe_2: tuple[int, int]) -> bool:
    pipe_1_sign = pipes_map[pipe_1[0]][pipe_1[1]]
    pipe_2_sign = pipes_map[pipe_2[0]][pipe_2[1]]
    if pipe_1_sign == "." or pipe_2_sign == ".":
        return False
    if pipe_1[0] == pipe_2[0] and pipe_1[1] < pipe_2[1]:
        if pipe_1_sign in ["|", "J", "7"]:
            return False
        if pipe_1_sign in ["S", "-", "L", "F"]:
            return pipe_2_sign in ["-", "J", "7", "S"]
    if pipe_1[0] == pipe_2[0] and pipe_1[1] > pipe_2[1]:
        if pipe_1_sign in ["|", "L", "F"]:
            return False
        if pipe_1_sign in ["S", "-", "J", "7"]:
            return pipe_2_sign in ["-", "L", "F", "S"]
    if pipe_1[0] < pipe_2[0] and pipe_1[1] == pipe_2[1]:
        if pipe_1_sign in ["-", "L", "J"]:
            return False
        if pipe_1_sign in ["S", "|", "7", "F"]:
            return pipe_2_sign in ["|", "L", "J", "S"]
    if pipe_1[0] > pipe_2[0] and pipe_1[1] == pipe_2[1]:
        if pipe_1_sign in ["-", "7", "F"]:
            return False
        if pipe_1_sign in ["S", "|", "L", "J"]:
            return pipe_2_sign in ["S", "|", "7", "F"]


def pipes_to_pipe_signs(pipes_map: list[list[int]], pipes: list[tuple[int, int]]):
    return [pipes_map[row][col] for row, col in pipes]


def part_1():
    pipes_map = [list(row) for row in read_lines()]
    loop = [[find_s(pipes_map)]]
    loop_complete = False
    pipes_in_loop = set(loop[0])
    while not loop_complete:
        pipes = loop[-1]
        next_pipes = []
        for row, col in pipes:
            surrounding_pipes = find_surrounding_pipes(row, col, len(pipes_map), len(pipes_map[0]))
            for surr_pipe_row, surr_pipe_col in surrounding_pipes:
                if surr_pipe_row < len(pipes_map) and surr_pipe_col < len(pipes_map[surr_pipe_row]) \
                        and pipes_match(pipes_map, (row, col), (surr_pipe_row, surr_pipe_col)) \
                        and (surr_pipe_row, surr_pipe_col) not in pipes_in_loop:
                    next_pipes.append((surr_pipe_row, surr_pipe_col))
        next_pipes.sort()
        if len(next_pipes) > 0 and next_pipes not in loop:
            loop.append(next_pipes)
            for new_pipe in next_pipes:
                pipes_in_loop.add(new_pipe)
        else:
            loop_complete = True
    print(f'Part 1: {len(loop) - 1}')


part_1()
