# solution23.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def parse_line(line: str) -> tuple:
    """Parse the line into instruction parameters"""
    if ',' in line:
        instruction, move = line.split(',')
        move = int(move)
        instruction, register = instruction.split()
    elif 'jmp' in line:
        instruction, move = line.split()
        move = int(move)
        register = None
    else:
        instruction, register = line.split()
        move = None

    return instruction, register, move

def execute_instruction(instruction: str, register: str, 
                        move: int, registers: dict, index: int) -> int:
    """Execute the current instruction and set the target register value"""
    if instruction == 'hlf':
        registers[register] = registers[register] / 2
        index += 1
    elif instruction == 'tpl':
        registers[register] = registers[register] * 3
        index += 1
    elif instruction == 'inc':
        registers[register] += 1
        index += 1
    elif instruction == 'jmp':
        index += move
    elif instruction == 'jie':
        if registers[register] % 2 == 0:
            index += move
        else:
            index += 1
    elif instruction == 'jio':
        if registers[register] == 1:
            index += move
        else:
            index += 1

    return index

def part1(data: list, registers: dict, return_register: str='b') -> str:
    """Solve part 1"""

    index = 0
    while index < len(data):
        instruction, register, move = parse_line(data[index])
        index = execute_instruction(instruction, register, move,
                                    registers, index)

    return registers[return_register]

def part2(data: list, registers: dict, return_register: str='b') -> str:
    """Solve part 2"""

    index = 0
    while index < len(data):
        instruction, register, move = parse_line(data[index])
        index = execute_instruction(instruction, register, move,
                                    registers, index)

    return registers[return_register]

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    registers = {'a': 0, 'b': 0}
    solution1 = f"Part 1: {part1(data=data, registers=registers)}"
    registers = {'a': 1, 'b': 0}
    solution2 = f"Part 2: {part2(data=data, registers=registers)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))