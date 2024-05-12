# solution6.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse text input"""
    
    return [line for line in puzzle_input.split()]

def part1(data):
    """Solve part 1"""

    corrected_message = ''
    for i in range(len(data[0])):
        charlist = [item[i] for item in data]
        corrected_message += max(charlist, key=charlist.count)

    return corrected_message

def part2(data):
    """Solve part 2"""

    corrected_message = ''
    for i in range(len(data[0])):
        charlist = [item[i] for item in data]
        corrected_message += min(charlist, key=charlist.count)

    return corrected_message

def solve(puzzle_input):
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