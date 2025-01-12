# solution.py

import pathlib
import sys

from collections import defaultdict

def parse(puzzle_input: str):
    """Parse text input"""
    data = defaultdict(int)
    for stone in map(int, puzzle_input.split()):
        data[stone] += 1

    return data


def change_stone(number: int) -> list:
    digits = str(number)

    if number == 0:
        return [1]
    
    if len(digits) % 2 == 0:
        return [int(half) for half in (digits[:len(digits) // 2], 
                    digits[len(digits) // 2:])]
    
    return [number * 2024]


def blink(stones: list, blinks: int = 1) -> list:
    """Blink `blinks` times and update the stones"""
    if blinks < 0:
        raise ValueError
    
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for new_stone in change_stone(stone):
                new_stones[new_stone] += count
        stones = new_stones

    return stones


def part1(stones: list):
    """Solve part 1"""
    stones = blink(stones, 25)
    return f"Part 1: {sum(stones.values())}"


def part2(stones: list):
    """Solve part 2"""
    stones = blink(stones, 75)
    return f"Part 2: {sum(stones.values())}"


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))