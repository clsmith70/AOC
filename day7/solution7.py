# aoc_template.py

import pathlib
import sys
from gates import LogicGates
import numpy as np

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split('\n')]

def part1(data: list, outgate: str='a') -> str:
    """Solve part 1"""
    memory = dict()
    program = list()

    for line in data:
        instruction = line.split(' -> ')
        if str(instruction[0]).isdigit() and len(instruction) == 2:
            memory[instruction[1]] = np.uint16(instruction[0])
        else:
            program.append(instruction)
    
    gates = LogicGates(memory, program)
    while True:
        gates.run()
        if gates.test_gate(outgate):
            break

    return gates.get_gate(outgate)

def part2(data: list, ingate: str, ingate_value: np.uint16, outgate: str='a') -> str:
    """Solve part 2"""
    memory = dict()
    program = list()

    for line in data:
        instruction = line.split(' -> ')
        if str(instruction[0]).isdigit() and len(instruction) == 2:
            memory[instruction[1]] = np.uint16(instruction[0])
        else:
            program.append(instruction)

    memory[ingate] = ingate_value

    gates = LogicGates(memory, program)
    while True:
        gates.run()
        if gates.test_gate(outgate):
            break

    return gates.get_gate(outgate)

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data)}"
    solution2 = f"Part 2: {part2(data=data, ingate='b', ingate_value=np.uint16(solution1.split()[-1]))}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))