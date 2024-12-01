# aoc_template.py

import pathlib
import sys

def parse(puzzle_input: str):
    """Parse text input"""
    return list(puzzle_input.split('\n'))

def part1(data: list):
    """Solve part 1"""
    return data

def part2(data: list):
    """Solve part 2"""
    return data

def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))