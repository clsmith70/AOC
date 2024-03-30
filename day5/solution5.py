# solution5.py

import pathlib
import re
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return [line for line in puzzle_input.split()]

def get_char_count(string: str, matchset: str):
    """Get count of characters in a matchset"""
    
    # ensure the entire string is lowercase
    string = string.casefold()
    # create a dict of matchset chars with initial count of 0
    count = {}.fromkeys(matchset, 0)
    # loop over characters and count them
    for character in string:
        # as long as they are in the matchset
        if character in count:
            count[character] += 1
    
    return sum(count.values())

def check_nice(string: str):
    """Check for part2 niceness"""

    # string is not nice if there aren't at least 2 
    # occurrences of the same double
    if not any([string[i] == string[i + 2] for i in range(len(string) - 2)]):
        return False
    # string is nice if it includes one alternating set of chars
    # ex: aba or xmx
    if any([(string.count(string[i: i + 2]) >= 2) \
            for i in range(len(string) -2)]):
        return True
    return False

def part1(data: list) -> str:
    """Solve part 1"""

    nice_count = 0
    regexA = re.compile(r"(.)\1")
    regexB = re.compile('ab|cd|pq|xy')

    # loop over the lines
    for line in data:
        # rule: string must contain at least 3 vowels
        if get_char_count(line, 'aeiou') >= 3:
            # rule: the string must have at least one double
            if regexA.findall(line):
                # rule: the string does not contain any illegal groups
                if not regexB.findall(line):
                    nice_count += 1

    return nice_count

def part2(data: list) -> str:
    """Solve part 2"""

    nice_count = 0

    # loop over the lines
    for line in data:
        # if they are nice
        if check_nice(line):
            # count them
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