# solution12.py

import json
import sys

def process_dict(data: str, total: int, part: int) -> int:
    if part == 1:
        for _, value in data.items():
            if type(value) == type(dict()):
                total = process_dict(value, total, part)
            elif type(value) == type(list()):
                total = process_list(value, total, part)
            elif type(value) == type(int()):
                total += int(value)
    elif part == 2:
        if not 'red' in data.values():
            for _, value in data.items():
                if type(value) == type(dict()):
                    total = process_dict(value, total, part)
                elif type(value) == type(list()):
                    total = process_list(value, total, part)
                elif type(value) == type(int()):
                    total += int(value)

    return total

def process_list(data: str, total: int, part: int) -> int:
    for key in data:
        if type(key) == type(dict()):
            total = process_dict(key, total, part)
        elif type(key) == type(list()):
            total = process_list(key, total, part)
        elif type(key) == type(int()):
            total += key
    
    return total

def part1(data: str) -> str:
    """Solve part 1"""
    total = 0
    total = process_dict(data, total, 1)
    return total

def part2(data: list) -> str:
    """Solve part 2"""
    total = 0
    total = process_dict(data, total, 2)
    return total

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""
    solution1 = f"Part 1: {part1(data=puzzle_input)}"
    solution2 = f"Part 2: {part2(data=puzzle_input)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        with open(path, 'r') as accounting_file:
            puzzle_input = json.load(accounting_file)
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))