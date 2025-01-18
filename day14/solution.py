# solution.py

import pathlib
import re
import sys

def parse(puzzle_input: str) -> tuple[list, int, int]:
    """Parse text input"""
    if len(puzzle_input.splitlines()) == 500:
        width, height = 101, 103
    else:
        width, height = 11, 7
    bots = [[*map(int, re.findall(r'-?\d+', line))] 
            for line in puzzle_input.splitlines()]
    
    return bots, width, height


def move_bots(iteration: int, bots: list, width: int, height: int) -> int:
    """Move the bots for this second"""
    q1, q2, q3, q4 = 0, 0, 0, 0

    for x, y, vx, vy in bots:
        x = (x + vx * iteration) % 101
        y = (y + vy * iteration) % 103

        q1 += x > width // 2 and y > height // 2
        q2 += x > width // 2 and y < height // 2
        q3 += x < width // 2 and y > height // 2
        q4 += x < width // 2 and y < height // 2

    return q1 * q2 * q3 * q4


def part1(bots: list, width: int, height: int):
    """Solve part 1"""

    return f"Part 1: {move_bots(100, bots, width, height)}"


def part2(bots: list, width: int, height: int):
    """Solve part 2"""

    return f"Part 2: {min(range(10_000), 
                    key=lambda i: move_bots(i, bots, width, height))}"


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data, w, h = parse(puzzle_input=puzzle_input)
    solution1 = part1(data, w, h)
    solution2 = part2(data, w, h)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))