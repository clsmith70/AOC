# solution24.py

import math
import pathlib
import sys
from itertools import combinations

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [int(line) for line in puzzle_input.split('\n')]

def pack_sleigh(data: list, groups: int) -> int:
    """Group packages into evenly weighted groups"""

    group_size = sum(data) // groups
    for i in range(len(data)):
        quantum_score = [math.prod(c) for c in combinations(data, i)
                         if sum(c) == group_size]
        if quantum_score:
            return min(quantum_score)

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {pack_sleigh(data=data, groups=3)}"
    solution2 = f"Part 2: {pack_sleigh(data=data, groups=4)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))