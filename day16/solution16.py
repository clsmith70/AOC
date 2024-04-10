# solution16.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def part1(data: list, ticker: dict) -> str:
    """Solve part 1"""

    for line in data:
        sue, values = line.split(':', 1)
        # get Sue's number
        sue = int(sue.split()[1])
        # get this Sue's "things"
        values = values.split(',')

        match = True
        for i in range(len(values)):
            key, value = values[i].split(':')
            key = key.strip()

            if key in ticker.keys():
                if not ticker[key] == int(value):
                    match = False

        if match:
            return sue

def part2(data: list, ticker: dict) -> str:
    """Solve part 2"""

    for line in data:
        sue, values = line.split(':', 1)
        # get Sue's number
        sue = int(sue.split()[1])
        # get this Sue's "things"
        values = values.split(',')

        match = True
        for i in range(len(values)):
            key, value = values[i].split(':')
            key = key.strip()

            if key in ticker.keys():
                if key == 'cats' or key == 'trees':
                    if not ticker[key] < int(value):
                        match = False
                elif key == 'pomeranians' or key == 'goldfish':
                    if not ticker[key] > int(value):
                        match = False
                elif not ticker[key] == int(value):
                    match = False

        if match:
            return sue

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    ticker = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
          'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
          'cars': 2, 'perfumes': 1}
    
    solution1 = f"Part 1: {part1(data=data, ticker=ticker)}"
    solution2 = f"Part 2: {part2(data=data, ticker=ticker)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))