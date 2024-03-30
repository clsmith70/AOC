# solution7.py

import pathlib
import sys
from gates import LogicGates
import numpy as np

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return [line for line in puzzle_input.split('\n')]

def part1(data: list, outgate: str='a') -> str:
    """Solve part 1"""

    # create memory dict and program list
    memory = dict()
    program = list()

    # for each line of data
    for line in data:
        # split the instruction on ->
        instruction = line.split(' -> ')
        # if the first character is a digit and it is 2 elements long
        if str(instruction[0]).isdigit() and len(instruction) == 2:
            # set the memory location to the value provided
            # converting the value to numpy uint16
            memory[instruction[1]] = np.uint16(instruction[0])
        else:
            # otherwise, append to the instruction set
            program.append(instruction)
    
    # create the logic gates with the initial memory and program values
    gates = LogicGates(memory, program)
    # until our requirement is met
    while True:
        # run the program
        gates.run()
        # if our interesting gate has a value
        if gates.test_gate(outgate):
            # stop
            break

    # return the interesting gate value
    return gates.get_gate(outgate)

def part2(data: list, ingate: str, ingate_value: np.uint16, \
          outgate: str='a') -> str:
    """Solve part 2"""

    # create memory dict and program list
    memory = dict()
    program = list()

    # for each line of data
    for line in data:
        # split the instruction on ->
        instruction = line.split(' -> ')
        # if the first character is a digit and it is 2 elements long
        if str(instruction[0]).isdigit() and len(instruction) == 2:
            # set the memory location to the value provided
            # converting the value to numpy uint16
            memory[instruction[1]] = np.uint16(instruction[0])
        else:
            # otherwise, append to the instruction set
            program.append(instruction)

    # override the appropriate gate with the directed value
    memory[ingate] = ingate_value

    # create the logic gates with the initial memory and program values
    gates = LogicGates(memory, program)
    # until our requirement is met
    while True:
        # run the program
        gates.run()
        # if our interesting gate has a value
        if gates.test_gate(outgate):
            # stop
            break

    # return the interesting gate value
    return gates.get_gate(outgate)

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data)}"
    solution2 = f"Part 2: {part2(data=data, ingate='b', \
                    ingate_value=np.uint16(solution1.split()[-1]))}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))