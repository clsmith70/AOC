# solution9.py

import pathlib
import sys
import re

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def decompress(line: str, V2: bool=False) -> int:
    """Decompress the line presented"""

    # if there is no marker, return the length of the string
    if '(' not in line:
        return len(line)
    
    # track the length of the decompressed string
    decomp_len = 0
    
    # while there are still SOM tags present
    while '(' in line:
        # find the first occurrence
        decomp_len += line.find('(')
        # remove any preceeding chars
        line = line[line.find('('):]
        # capture the marker values
        length, repeat = line[1:line.find(')')].split('x')
        length = int(length)
        repeat = int(repeat)
        # remove the marker
        line = line[line.find(')') + 1:]

        # if version 2 compression is used
        if V2:
            # expand the additional markers in the section
            decomp_len += decompress(line[:length], V2) * repeat
        else:
            # ignore contained markers (V1)
            decomp_len += len(line[:length]) * repeat
        
        # remove chars referenced by the marker
        line = line[length:]
    # update the decompressed length
    decomp_len += len(line)

    return decomp_len

def part1(data: list) -> str:
    """Solve part 1"""

    decompressed_length = 0
    for line in data:
        decompressed_length += decompress(line)

    return decompressed_length

def part2(data: list) -> str:
    """Solve part 2"""

    decompressed_length = 0
    for line in data:
        decompressed_length += decompress(line, V2=True)

    return decompressed_length

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