# solution18.py

import pathlib
import sys

import numpy as np
from scipy.ndimage import generic_filter

def parse(puzzle_input: str) -> np.array:
    """Parse text input"""

    array_size = len(puzzle_input.split('\n'))
    data_grid = np.zeros((array_size, array_size), dtype='int')
    for row, line in enumerate(puzzle_input.split('\n')):
        data_row = [{'#': 1, '.': 0}[i] for i in line.strip()]
        data_grid[row] = data_row
    
    return data_grid

def light_state(neighbor_grid: np.array) -> int:
    """Alters the state of the middle light based on neighbors"""

    # get the light in the middle of the grid
    light = neighbor_grid[4]
    # sum the lights that are on
    on = np.sum(neighbor_grid)
    # if the light is on and 2 or 3 neighbors are on, leave it on
    if light:
        if on == 3 or on == 4: # add one for the target light
            return 1
        else:
            return 0
    else: # if exactly 3 neighbors are lit, turn it on
        if on == 3:
            return 1
        else:
            return 0
        
def toggle_grid(grid, steps, part) -> np.array:
    """Toggles light states in the grid"""

    for _ in range(steps):
        # create a new 3x3 grid using scipy.ndimage.generic_filter
        new_grid = generic_filter(grid, light_state, size=3, mode='constant')
        if part == 2: # four corners are stuck on
            new_grid[0, 0] = 1
            new_grid[0, -1] = 1
            new_grid[-1, 0] = 1
            new_grid[-1, -1] = 1
        grid = new_grid # replace the grid
    return grid

def part1(data: np.array, number_of_steps: int) -> str:
    """Solve part 1"""

    grid = toggle_grid(data, number_of_steps, 1)
    return np.sum(grid)

def part2(data: np.array, number_of_steps: int) -> str:
    """Solve part 2"""

    grid = toggle_grid(data, number_of_steps, 2)
    return np.sum(grid)

def solve(puzzle_input: str, steps: int) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data, number_of_steps=steps)}"
    solution2 = f"Part 2: {part2(data=data, number_of_steps=steps)}"

    return solution1, solution2

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\nUsage:   python solution18.py data_file number_of_steps")
        print("Example: python solution18.py input.txt 100\n\n")
    else:
        path = sys.argv[1]
        steps = int(sys.argv[2])
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input, steps=steps)
        print("\n".join(str(solution) for solution in solutions))