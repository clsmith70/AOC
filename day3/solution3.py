# solution3.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse text input"""

    return [line for line in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""

    # track the number of valid triangles
    valid_count = 0

    for line in data:
        # split the sides into a list of integers
        sides = [int(s) for s in line.split()]
        # sort the sides and split them
        a, b, c = sorted(sides)
        # if the sum of the two shorter sides is greater than the longer
        if a + b > c:
            # it is valid
            valid_count += 1

    return valid_count

def part2(data):
    """Solve part 2"""

    # track the number of valid triangles
    valid_count = 0

    # loop over every three rows of data
    for i in range(0, len(data), 3):
        # split each of the 3 lines into lists of integer sides
        a_sides = [int(a) for a in data[i].split()]
        b_sides = [int(b) for b in data[i + 1].split()]
        c_sides = [int(c) for c in data[i + 2].split()]

        # loop over the three sets of sides
        for j in range(3):
            # sort the sides and split them
            a, b, c = sorted([a_sides[j], b_sides[j], c_sides[j]])
            # if the sum of the two shorter sides is greater than the longer
            if a + b > c:
                # it is valid
                valid_count += 1

    return valid_count

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