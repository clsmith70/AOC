# solution2.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse text input"""

    return [line for line in puzzle_input.split()]

def check_key(button: tuple, keypad: list) -> bool:
    """Check if the button is valid"""

    # separate the button coordinates
    y, x = button
    # if the location is a non-button location
    if keypad[y][x] == 'X':
        # return false
        return False
    # otherwise, return true
    return True

def next_button(button: tuple, direction: str, keypad: list) -> tuple:
    """Get the button at next position"""

    # set the min and max range of the keypad
    min_range = 0
    max_range = len(keypad) - 1
    # separate the button coordinates
    y, x = button

    # check which direction to move
    if direction == 'U':
        # go up, subtracting from y
        y -= 1
        # if y is below the minimum range, set it to the minimum
        if y < min_range:
            y = min_range
        # if the location is a non-button, go down a step
        if not check_key((y, x), keypad):
            y += 1

    elif direction == 'D':
        # go down, adding to y
        y += 1
        # if y is above the maximum range, set it to the maximum
        if y > max_range:
            y = max_range
        # if the location is a non-button, go up a step
        if not check_key((y, x), keypad):
            y -= 1

    elif direction == 'L':
        # go left, subtracting from x
        x -= 1
        # if x is below the minimum range, set it to the minimum
        if x < min_range:
            x = min_range
        # if the location is a non-button, go right a step
        if not check_key((y, x), keypad):
            x += 1

    elif direction == 'R':
        # go right, adding to x
        x += 1
        # if x is above the maximum range, set it to the maximum
        if x > max_range:
            x = max_range
        # if the location is a non-button, go left a step
        if not check_key((y, x), keypad):
            x -= 1

    return y, x

def part1(data):
    """Solve part 1"""

    # set the expected keypad layout
    keypad = [
        ['1', '2', '3'], 
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    # initialize the code and set the first button coordinates
    code = ""
    button = (1, 1) # the 5 button in the center

    for line in data:
        for char in line:
            # get the next button for the current step
            button = next_button(button, char, keypad)
        # once the line is complete, get the coordinates of the button
        y, x = button
        # add the button to the code
        code += keypad[y][x]

    return code

def part2(data):
    """Solve part 2"""

    # set the actual keypad layout
    keypad = [
        ['X', 'X', '1', 'X', 'X'],
        ['X', '2', '3', '4', 'X'],
        ['5', '6', '7', '8', '9'],
        ['X', 'A', 'B', 'C', 'X'],
        ['X', 'X', 'D', 'X', 'X']
    ]

    # initialize the code and set the first button coordinates
    code = ""
    button = (2, 0)

    for line in data:
        for char in line:
            # get the next button for the current step
            button = next_button(button, char, keypad)
        # once the line is complete, get the coordinates of the button
        y, x = button
        # add the button to the code
        code += keypad[y][x]

    return code

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