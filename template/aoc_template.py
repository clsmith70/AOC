# aoc_template.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split()]

def part1(data: list) -> str:
    """Solve part 1"""
    return ""

def part2(data: list) -> str:
    """Solve part 2"""
    return ""

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data)}"
    solution2 = f"Part 2: {part2(data=data)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_data = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_data)
        print("\n".join(str(solution) for solution in solutions))
