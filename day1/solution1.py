# solution1.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse text input"""
    
    return [dir.strip() for dir in puzzle_input.split(',')]

def turn(direction: str, compass: int) -> int:
    """Make the directed 90 degree turn and set the compass"""

    if direction == 'R':
        # positive 90 degree turn
        compass += 90
        if compass >= 360:
            compass -= 360

    elif direction == 'L':
        # negative 90 degree turn
        compass -= 90
        if compass < 0:
            compass += 360

    return compass

def move(x: int, y: int, compass: int, blocks: int) -> tuple:
    """Move the number of blocks in the current direction"""

    if compass == 0:
        # go north
        y += blocks
    elif compass == 90:
        # go east
        x += blocks
    elif compass == 180:
        # go south
        y -= blocks
    elif compass == 270:
        # go west
        x -= blocks

    return x, y

def part1(data):
    """Solve part 1"""

    x, y, compass = 0, 0, 0
    for direction in data:
        heading, blocks = direction[0], int(direction[1:])
        compass = turn(heading, compass)
        x, y = move(x, y, compass, blocks)

    return abs(x) + abs(y)

def part2(data):
    """Solve part 2"""
    
    grid = {}
    coordinates = [(x, y) for x in range(-300, 301)
                   for y in range(-300, 301)]
    for c in coordinates:
        grid[c] = 0

    x, y, compass = 0, 0, 0
    grid[(x, y)] += 1

    for direction in data:
        heading, blocks = direction[0], int(direction[1:])
        compass = turn(heading, compass)
        for _ in range(blocks):
            x, y = move(x, y, compass, 1)
            grid[(x, y)] += 1
        
            if grid[(x, y)] > 1:
                return abs(x) + abs(y)

def solve(puzzle_input):
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