# aoc_template.py

import pathlib
import sys
from itertools import permutations

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split('\n')]

def add_location(source: str, destination: str, distance: int, location_dict: dict) -> dict:
    
    if source in location_dict.keys(): location_dict[source].append((destination, distance))
    else: location_dict[source] = [(destination, distance)]

    if destination in location_dict.keys(): location_dict[destination].append((source, distance))
    else: location_dict[destination] = [(source, distance)]
    
def path_distance(path: tuple, location_dict: dict) -> int:
    total = 0
    path = list(path)

    while len(path) > 1:
        current = path.pop(0)
        destinations = location_dict[current]

        for (distance, cost) in destinations:
            if distance == path[0]:
                total += cost
                break

    return total

def part1(data: list) -> str:
    """Solve part 1"""
    location_dict = dict()
    shortest_distance = 999999999

    for line in data:
        source, _, destination, _, distance = line.split()
        add_location(source, destination, int(distance), location_dict)
 
    for path in permutations(location_dict.keys()):
        trip = path_distance(path, location_dict)
        if trip < shortest_distance:
            shortest_distance = trip

    return shortest_distance

def part2(data: list) -> str:
    """Solve part 2"""
    location_dict = dict()
    longest_distance = 0

    for line in data:
        source, _, destination, _, distance = line.split()
        add_location(source, destination, int(distance), location_dict)
 
    for path in permutations(location_dict.keys()):
        trip = path_distance(path, location_dict)
        if trip > longest_distance:
            longest_distance = trip

    return longest_distance


def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data)}"
    solution2 = f"Part 2: {part2(data=data)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))