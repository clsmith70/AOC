# aoc_template.py

import pathlib
import re
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split()]

def get_char_count(string: str, matchset: str):
    """Get count of characters in a matchset"""
    string = string.casefold() # ensure the entire string is lowercase
    count = {}.fromkeys(matchset, 0)
    for character in string:
        if character in count:
            count[character] += 1
    
    return sum(count.values())

def check_nice(string: str):
    """Check for part2 niceness"""
    if not any([string[i] == string[i + 2] for i in range(len(string) - 2)]):
        return False
    if any([(string.count(string[i: i + 2]) >= 2) for i in range(len(string) -2)]):
        return True
    return False

def part1(data: list) -> str:
    """Solve part 1"""
    nice_count = 0
    regexA = re.compile(r"(.)\1")
    regexB = re.compile('ab|cd|pq|xy')

    for line in data:
        if get_char_count(line, 'aeiou') >= 3:
            if regexA.findall(line):
                if not regexB.findall(line):
                    nice_count += 1

    return nice_count

def part2(data: list) -> str:
    """Solve part 2"""
    nice_count = 0

    for line in data:
        if check_nice(line):
            nice_count += 1

    return nice_count

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