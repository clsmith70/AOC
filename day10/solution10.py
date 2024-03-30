# solution10.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return puzzle_input

def look(value):
    result = ""
    while not value == "":
        (said, value) = say(value)
        result += said
    return result

def say(value: str) -> str:
    x = value[0]
    count = 0

    for char in value:
        if char == x:
            count += 1
        else:
            break

    rest = value[count:]
    return (str(count) + x, rest)

def part1(data: str, iterations: int=40) -> str:
    """Solve part 1"""
    num = data
    for _ in range(iterations):
        num = look(num)

    return len(num)

def part2(data: str, iterations: int=50) -> str:
    """Solve part 2"""
    num = data
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