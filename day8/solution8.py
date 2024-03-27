# aoc_template.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split()]

def part1(data: list) -> str:
    """Solve part 1"""
    code_chars, mem_chars = 0, 0

    for line in data:
        code_chars += len(line)
        mem_chars += len(eval(line))

    return (code_chars - mem_chars)

def part2(data: list) -> str:
    """Solve part 2"""
    code_chars, encoded_chars = 0, 0

    for line in data:
        code_chars += len(line)
        encoded_chars += line.count('\\') + line.count('"') + 2

    return encoded_chars

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