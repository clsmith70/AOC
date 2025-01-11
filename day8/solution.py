# solution.py

import pathlib
import sys

from collections import defaultdict


def parse(puzzle_input: str):
    """Parse text input"""
    return [list(map(str, line)) for line in puzzle_input.split('\n')]


def in_bounds(area: list, x: int, y: int) -> bool:
    # test if the coordinates are within the bounds of the area map
    return 0 <= x < len(area[0]) and 0 <= y < len(area)


def get_antennas(data: list) -> defaultdict:
    # return a list of antennas and their coordinates
    antennas = defaultdict(list)

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == ".":
                continue
            antennas[data[y][x]].append((x, y))

    return antennas


def get_antinodes(data, node1, node2):
    # get the antinodes for the antenna
    points1 = set()
    points2 = {node1, node2}

    x1, y1 = node1
    x2, y2 = node2
    x_dist = x2 - x1
    y_dist = y2 - y1

    if in_bounds(data, x1 - x_dist, y1 - y_dist):
        points1.add((x1 - x_dist, y1 - y_dist))
    if in_bounds(data, x2 + x_dist, y2 + y_dist):
        points1.add((x2 + x_dist, y2 + y_dist))

    thisX, thisY = x1, y1
    while True:
        thisX -= x_dist
        thisY -= y_dist
        if not in_bounds(data, thisX, thisY):
            break
        points2.add((thisX, thisY))

    thisX, thisY = x1, y1
    while True:
        thisX += x_dist
        thisY += y_dist
        if not in_bounds(data, thisX, thisY):
            break
        points2.add((thisX, thisY))

    return points1, points2


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    antenna_list = get_antennas(data)
    part1 = set()
    part2 = set()
    for value in antenna_list.values():
        for i in range(len(value)):
            for j in range(i + 1, len(value)):
                points1, points2 = get_antinodes(data, value[i], value[j])
                part1.update(points1)
                part2.update(points2)

    solution1 = f"Part 1: {len(part1)}"
    solution2 = f"Part 2: {len(part2)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))