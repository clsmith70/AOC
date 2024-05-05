# solution25.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input: str) -> tuple:
    """Parse text input"""
    
    temp = puzzle_input.split('row')
    temp = temp[1].split(', column')
    row, column = int(temp[0]), int(temp[1].split('.')[0])
    
    return row, column

def part1(start: int, row: int, column: int) -> str:
    """Solve part 1"""

    start_code = np.sum(np.arange(2, column + 1)) + 1
    code_number = start_code + np.sum(
        np.arange(column, column + row - 1)
    )

    for _ in range(code_number - 1):
        start = (start * 252533) % 33554393

    return start

def part2() -> str:
    """Solve part 2"""

    return "Power Cycle the machine and have a Merry Christmas!"

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    row, column = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(20151125, row, column)}"
    solution2 = f"Part 2: {part2()}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))