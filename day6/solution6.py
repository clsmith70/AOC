# soution6.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return [line for line in puzzle_input.split('\n')]

def set_grid(action: str, startX: int, startY: int,
               endX: int, endY: int, grid: np.array, part1: bool=True):
    """Set the grid light states"""

    # loop through the x and y ranges
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            # for part 1
            if part1:
                # turn lights on
                if action == 'on':
                    grid[x, y] = 1
                # turn lights off
                elif action == 'off':
                    grid[x, y] = 0
                # swap light state on -> off or off -> on
                elif action == 'toggle':
                    if grid[x, y] == 1:
                        grid[x, y] = 0
                    else:
                        grid[x, y] = 1
            # for part 2
            else:
                # increase brightness
                if action == 'on':
                    grid[x, y] += 1
                elif action == 'off':
                    # decrease brightness
                    if grid[x, y] > 1:
                        grid[x, y] -= 1
                    # or turn off/leave off
                    else:
                        grid[x, y] = 0
                # increase brightness by 2
                elif action == 'toggle':
                    grid[x, y] += 2

def part1(data: list) -> str:
    """Solve part 1"""

    # create a zero based integer light grid
    lights = np.zeros((1000, 1000), dtype=np.uint32)

    # for each line of data
    for line in data:
        # split the values based on the first part of the line
        if line.startswith('toggle'):
            action, start, _, end = line.split()
        else:
            _, action, start, _, end = line.split()

        # map the start and end values to int values
        startX, startY = list(map(int, start.split(',')))
        endX, endY = list(map(int, end.split(',')))

        # set the light states of the grid
        set_grid(action, startX, startY, endX, endY, lights)

    # count a sum of lights that are on
    return np.sum(lights)

def part2(data: list) -> str:
    """Solve part 2"""

    # create a zero based integer light grid
    lights = np.zeros((1000, 1000), dtype=np.uint32)

    # for each line of data
    for line in data:
        # split the values based on the first part of the line
        if line.startswith('toggle'):
            action, start, _, end = line.split()
        else:
            _, action, start, _, end = line.split()

        # map the start and end values to int values
        startX, startY = list(map(int, start.split(',')))
        endX, endY = list(map(int, end.split(',')))

        # set the light states of the grid
        set_grid(action, startX, startY, endX, endY, lights, part1=False)

    # sum the brightness of the grid
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