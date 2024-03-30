# solution1.py

import pathlib
import sys

def parse(puzzle_input: str):
    """Parse text input"""

    return puzzle_input

def part1(data: str):
    """Solve part 1"""

    floor: int = 0

    # loop through the instructions
    for char in data:
        # go up if char is (
        if char == '(':
            floor += 1
        # do down if char is )
        elif char == ')':
            floor -= 1
    
    return floor

def part2(data: str):
    """Solve part 2"""

    basement_entry: int = 0
    is_basement = False
    floor: int = 0

    # loop through the instructions
    for char in data:
        # track the instruction count for basement entry
        basement_entry += 1
        # go up if char is (
        if char == '(':
            floor += 1
        # go down if char is )
        elif char == ')':
            floor -= 1

        # if we have not found the basement yet and the floor is < 0
        if is_basement == False and floor < 0:
            # return the instruction count
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