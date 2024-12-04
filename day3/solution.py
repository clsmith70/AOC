# solution.py

import pathlib
import re
import sys

def parse(puzzle_input: str):
    """Parse text input"""
    return list(puzzle_input.split('\n'))

def part1(data: list):
    """Solve part 1"""
    part1_sum = 0
    # create a regex to find the mul() pattern in each line
    regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    # find the matches in each line of input
    for line in data:
        matches = regex.findall(line)
        # evaluate each match and add the result to the sum
        for match in matches:
            x, y = map(int, match[4:-1].split(","))
            part1_sum += x * y

    return part1_sum

def part2(data: str):
    """Solve part 2"""
    part2_sum = 0

    # create a regex to find the mul() pattern in each line
    # as well as the do() and don't() patterns
    regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    matches = regex.findall(data)
    process = True
    for match in matches:
        if match == "do()":
            process = True
        elif match == "don't()":
            process = False
        else:
            if process:
                x, y = map(int, match[4:-1].split(","))
                part2_sum += x * y

    return part2_sum

def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = part1(data)
    solution2 = part2(puzzle_input)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))