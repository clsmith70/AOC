# solution19.py

import pathlib
import sys
from random import shuffle

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line.strip() for line in puzzle_input.split('\n')]

def swap(molecule: str, position: int, source: str, destination: str) -> list:
    """swap source and destination elements in the provided molecule"""

    return molecule[:position] + destination + \
          molecule[position + len(source):]

def replace_molecule(molecule: str, replacement: str, position: int,
                medicine: set) -> set:
    """Replace elements in the medicine molecule"""

    source, destination = replacement
    position = molecule.find(source, position)

    while position != -1:
        result = swap(molecule, position, source, destination)
        medicine.add(result)
        position = molecule.find(source, position + 1)

def part1(data: list) -> str:
    """Solve part 1"""
    
    medicine = set()
    molecule = data[-1]
    instructions = [d.split(' => ') for d in data[:-2]]

    for rep in instructions:
        replace_molecule(molecule, rep, position=0, medicine=medicine)

    return len(medicine)

def part2(data: list) -> str:
    molecule = data[-1]
    instructions = [(d.split(' => ')) for d in data[:-2]]

    target = molecule
    steps = 0

    while target != 'e':
        temp = target
        for a, b in instructions:
            if b not in target:
                continue

            target = target.replace(b, a, 1)
            steps += 1

        if temp == target:
            target = molecule
            steps = 0
            shuffle(instructions)

    return steps


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