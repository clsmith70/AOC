# solution2.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split()]

def part1(data: list) -> str:
    """Solve part 1"""
    total_area: int = 0

    for line in data:
        l, w, h = list(map(int, line.split('x')))
        side1 = l * w
        side2 = w * h
        side3 = h * l

        area = (2 * side1) + (2 * side2) + (2 * side3)
        slack = min(side1, side2, side3)
        total_area += area + slack
    
    return total_area

def part2(data: list) -> str:
    """Solve part 2"""
    total_ribbon: int = 0

    for line in data:
        l, w, h = list(map(int, line.split('x')))
        sorted_sides = sorted([l, w, h])

        cur_ribbon = (sorted_sides[0] * 2) + (sorted_sides[1] * 2)
        cur_bow = l * w * h

        total_ribbon += cur_ribbon + cur_bow

    return total_ribbon

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