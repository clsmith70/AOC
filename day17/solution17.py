# solution17.py

import pathlib
import sys

from itertools import combinations

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [int(line) for line in puzzle_input.split('\n')]

def part1(data: list, liters_to_store: int) -> str:
    """Solve part 1"""

    set_count = 0

    for i in range(len(data)):
        for set in combinations(data, i):
            if sum(list(set)) == liters_to_store:
                set_count += 1

    return set_count

def part2(data: list, liters_to_store: int) -> str:
    """Solve part 2"""

    set_count = {}

    for i in range(len(data)):
        for set in combinations(data, i):
            if sum(list(set)) == liters_to_store:
                setlen = len(set)
                if setlen not in set_count.keys():
                    set_count[setlen] = 1
                else:
                    set_count[setlen] += 1

    return set_count[min(set_count.keys())]

def solve(puzzle_input: str, liters: int) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data, liters_to_store=liters)}"
    solution2 = f"Part 2: {part2(data=data, liters_to_store=liters)}"

    return solution1, solution2

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\nUsage:   python solution17.py data_file number_of_liters")
        print("Example: python solution17.py input.txt 150\n\n")
    else:
        path = sys.argv[1]
        liters = int(sys.argv[2])
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input, liters=liters)
        print("\n".join(str(solution) for solution in solutions))