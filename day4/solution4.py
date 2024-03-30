# solution4.py

import pathlib
import sys
from hashlib import md5

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return puzzle_input

def part1(data: list) -> str:
    """Solve part 1"""

    integer = 0
    # loop until our condition is met
    while True:
        # append the integer to the data
        hashtest = data + str(integer)
        # calculate the md5sum
        md5sum = md5(hashtest.encode('utf-8')).hexdigest()
        # check if is starts with 5 zeros
        if md5sum.startswith('00000'):
            # if it does, leave
            break
        else:
            # if not, add one more and try again
            integer += 1

    return integer

def part2(data: list) -> str:
    """Solve part 2"""

    integer = 0
    # loop until our condition is met
    while True:
        # append the integer to the data
        hashtest = data + str(integer)
        # calculate the md5sum
        md5sum = md5(hashtest.encode('utf-8')).hexdigest()
        # check if is starts with 6 zeros
        if md5sum.startswith('000000'):
            # if it does, leave
            break
        else:
            # if not, add one more and try again
            integer += 1

    return integer

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