# solution3.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return puzzle_input

def add_house(x: int, y: int, coordinates: list):
    """Create a house coordinate"""

    house = (x, y)
    # if the house is not in coordinates, add it
    if house not in coordinates:
        coordinates.append(house)

def part1(data: list) -> str:
    """Solve part 1"""

    startX, startY = 0, 0
    coords = []
    # add the starting coordinate
    add_house(startX, startY, coords)

    # loop over directions
    for dir in data:
        # move north
        if dir == '^':
            startY += 1
        # move south
        elif dir == 'v':
            startY -= 1
        # move west
        elif dir == '<':
            startX -=1
        # move east
        elif dir == '>':
            startX += 1

        # add the newest coordinate
        add_house(startX, startY, coords)

    return len(coords)

def part2(data: list) -> str:
    """Solve part 2"""

    santaX, santaY = 0, 0
    roboX, roboY = 0, 0
    coords = []
    santa_turn = True
    # add the starting coordinate
    add_house(santaX, santaY, coords)

    # loop over the directions
    for dir in data:
        # move north
        if dir == '^':
            # update position based on whose turn it is
            if santa_turn:
                santaY += 1
            else:
                roboY += 1
        # move south
        elif dir == 'v':
            # update position based on whose turn it is
            if santa_turn:
                santaY -= 1
            else:
                roboY -= 1
        # move west
        elif dir == '<':
            # update position based on whose turn it is
            if santa_turn:
                santaX -=1
            else:
                roboX -=1
        # move east
        elif dir == '>':
            # update position based on whose turn it is
            if santa_turn:
                santaX += 1
            else:
                roboX += 1

        # add the coordinate to the list based on whose turn it is
        if santa_turn:
            add_house(santaX, santaY, coords)
        else:
            add_house(roboX, roboY, coords)
        
        # swap turns
        santa_turn = not santa_turn

    return len(coords)

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