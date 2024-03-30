# soution6.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split('\n')]

def set_grid(action: str, startX: int, startY: int,
               endX: int, endY: int, grid: np.array, part1: bool=True):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if part1:
                if action == 'on':
                    grid[x, y] = 1
                elif action == 'off':
                    grid[x, y] = 0
                elif action == 'toggle':
                    if grid[x, y] == 1:
                        grid[x, y] = 0
                    else:
                        grid[x, y] = 1
            else:
                if action == 'on':
                    grid[x, y] += 1
                elif action == 'off':
                    if grid[x, y] > 1:
                        grid[x, y] -= 1
                    else:
                        grid[x, y] = 0
                elif action == 'toggle':
                    grid[x, y] += 2

def part1(data: list) -> str:
    """Solve part 1"""
    lights = np.zeros((1000, 1000), dtype=np.uint32)

    for line in data:
        if line.startswith('toggle'):
            action, start, _, end = line.split()
        else:
            _, action, start, _, end = line.split()

        startX, startY = list(map(int, start.split(',')))
        endX, endY = list(map(int, end.split(',')))

        set_grid(action, startX, startY, endX, endY, lights)

    return np.sum(lights)

def part2(data: list) -> str:
    """Solve part 2"""
    lights = np.zeros((1000, 1000), dtype=np.uint32)

    for line in data:
        if line.startswith('toggle'):
            action, start, _, end = line.split()
        else:
            _, action, start, _, end = line.split()

        startX, startY = list(map(int, start.split(',')))
        endX, endY = list(map(int, end.split(',')))

        set_grid(action, startX, startY, endX, endY, lights, part1=False)

    return np.sum(lights)

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