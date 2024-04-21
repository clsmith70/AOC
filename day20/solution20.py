# solution20.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return int(puzzle_input)

def deliver(data: int, limit: int, multiplier: int = 10,
            delivery_limited: bool = False, delivery_limit: int = 50) -> str:
    """Solve part 1"""

    houses = np.zeros(limit + 1, dtype='int')

    elf = 1
    # limit elves and houses to the same number
    while elf <= limit:
        # the first house is the same number as the elf
        i = elf
        delivered = 0

        while i <= limit:
            if delivery_limited:
                if delivered > delivery_limit:
                    break

            houses[i] += elf * multiplier
            i += elf
            delivered += 1
        elf += 1

    for index in range(len(houses)):
        if houses[index] >= data:
            return index

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    part1 = deliver(data=data, limit=2500000)
    part2 = deliver(data=data, limit=2500000, multiplier=11, \
                    delivery_limited=True, delivery_limit=50)
    solution1 = f"Part 1: {part1}"
    solution2 = f"Part 2: {part2}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))