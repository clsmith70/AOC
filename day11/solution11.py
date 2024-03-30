# solution11.py

import pathlib
import re
import sys

VALID_CHARS = 'abcdefghjkmnpqrstuvwxyz'

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return [line for line in puzzle_input.split('\n')]

def test_password(password: str) -> bool:
    """Test password validity"""

    valid_pairs = [char + char for char in VALID_CHARS]
    straights = [''.join(c) for c in \
                 zip(VALID_CHARS[:-2], VALID_CHARS[1:-1], VALID_CHARS[2:])]

    # RULE1: cannot contain i, l, or o
    invalid_chars = r"ilo"
    if any(elem in password for elem in invalid_chars): return False
    # RULE2: must contain at least 2 double character sets
    if sum([pair in password for pair in valid_pairs]) < 2: return False
    # RULE3: must contain a straight of 3 or more consecutive valid chars
    if not any([run in password for run in straights]): return False

    return True

def next_password(password: str) -> str:
    """Find the next password"""

    next_letter = {char1: char2 for char1, char2 in \
                   zip(VALID_CHARS, VALID_CHARS[1:]+'a')}
    
    # add invalid chars to assure they are dealt with properly
    next_letter['i'] = 'j'
    next_letter['l'] = 'm'
    next_letter['o'] = 'p'

    # increment the last letter to initialize
    password = password[:-1] + next_letter[password[-1]]

    # loop over the chars from right to left, incrementing as needed
    for i in range(-1, -8, -1):
        # if the current letter is 'a', increment
        if password[i] == 'a':
            password = password[:i - 1] + \
                next_letter[password[i - 1]] + \
                password[i:]
        else:
            # otherwise stop
            break
        
    return password

def part1(data: list) -> str:
    """Solve part 1"""

    # get the first item in the list (should only be one)
    password = data[0]
    # as long as the password is not valid
    while test_password(password) == False:
        # get the next one
        password = next_password(password)
    
    return password

def part2(data: str) -> str:
    """Solve part 2"""

    # get the passed in password string
    password = next_password(data)
    # as long as the password is not valid
    while test_password(password) == False:
        # get the next one
        password = next_password(password)
    
    return password

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""
    
    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data)}"
    solution2 = f"Part 2: {part2(data=solution1.split(': ')[1])}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))