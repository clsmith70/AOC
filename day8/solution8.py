# solution8.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return [line for line in puzzle_input.split()]

def part1(data: list) -> str:
    """Solve part 1"""

    # set up counters for code and memory lengths
    code_chars, mem_chars = 0, 0

    # for each line of data
    for line in data:
        # count the number of code chars
        code_chars += len(line)
        # count the number of in-memory chars
        mem_chars += len(eval(line))

    # return the difference between the two
    return (code_chars - mem_chars)

def part2(data: list) -> str:
    """Solve part 2"""

    # set up a counter for encoded chars
    encoded_chars = 0

    # for each line of data
    for line in data:
        # count the number of encoded in-memory chars
        encoded_chars += line.count('\\') + line.count('"') + 2

    # return the encoded count
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