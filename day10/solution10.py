# solution10.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return puzzle_input

def look(value):
    """Look at the value"""

    result = ""
    # while we have a value available
    while not value == "":
        # say what is seen
        (said, value) = say(value)
        # add it to the result
        result += said

    return result

def say(value: str) -> str:
    """Say what is seen"""

    x = value[0]
    count = 0

    # loop over each character
    for char in value:
        # see how many of the same one are seen
        if char == x:
            # count it
            count += 1
        else:
            break

    # take the remaining non-matches
    rest = value[count:]

    # return the count of numbers and the remainder
    return (str(count) + x, rest)

def part1(data: str, iterations: int=40) -> str:
    """Solve part 1"""

    num = data
    # repeat the look-and-say process for the requested number of times
    for _ in range(iterations):
        num = look(num)

    return len(num)

def part2(data: str, iterations: int=50) -> str:
    """Solve part 2"""

    num = data
    # repeat the look-and-say process for the requested number of times
    for _ in range(iterations):
        num = look(num)

    return len(num)

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