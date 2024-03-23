# solution1.py

import pathlib
import sys

def parse(puzzle_input: str):
    """Parse text input"""
    return puzzle_input

def part1(data: str):
    """Solve part 1"""
    floor: int = 0

    for char in data:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    
    return floor

def part2(data: str):
    """Solve part 2"""
    basement_entry: int = 0
    is_basement = False
    floor: int = 0

    for char in data:
        basement_entry += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if is_basement == False and floor < 0:
            return basement_entry

def solve(puzzle_input: str):
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