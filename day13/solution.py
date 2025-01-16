# solution.py

import pathlib
import sys

import numpy as np

def parse(puzzle_input: str, convert: bool = False):
    """Parse text input"""
    convert_value = 10_000_000_000_000
    output = []
    for group in puzzle_input.split("\n\n"):
        data = {}
        a, b, prize = group.splitlines()
        data['A'] = [int(data.split('+')[1]) for data 
                    in a.split(':')[1].split(', ')]
        data['B'] = [int(data.split('+')[1]) for data 
                    in b.split(':')[1].split(', ')]
        data['Prize'] = [int(data.split('=')[1]) for data 
                    in prize.split(':')[1].split(', ')]
        if convert:
            data['Prize'][0] += convert_value
            data['Prize'][1] += convert_value
        output.append(data)


    return output


def get_button_presses(machine: dict) -> tuple[int, int] | None:
    """Try to win the prize and count the tokens required"""
    # split the machine values into integer values
    ax, ay = machine['A']
    bx, by = machine['B']
    px, py = machine['Prize']
    
    # solve the system of equations for the A button
    button_a, remainder = divmod(px * by - py * bx, ax * by - ay * bx)
    if remainder:
        return None
    
    # solve the system of equations for the B button
    button_b, remainder = divmod(px - ax * button_a, bx)
    if remainder:
        return None
    
    # check the system of equations
    assert ax * button_a + bx * button_b == px
    assert ay * button_a + by * button_b == py

    return button_a, button_b


def part1(data: list):
    """Solve part 1"""
    tokens = 0

    for machine in data:
        if (answer := get_button_presses(machine)) is not None:
            button_a, button_b = answer
            tokens += 3 * button_a + button_b

    return f"Part 1: {tokens}"


def part2(data: list):
    """Solve part 2"""
    tokens = 0

    for machine in data:
        if (answer := get_button_presses(machine)) is not None:
            button_a, button_b = answer
            tokens += 3 * button_a + button_b
    
    return f"Part 2: {tokens}"


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data1 = parse(puzzle_input=puzzle_input)
    data2 = parse(puzzle_input=puzzle_input, convert=True)
    solution1 = part1(data1)
    solution2 = part2(data2)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))