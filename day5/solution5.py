# solution5.py

import pathlib
import sys
from hashlib import md5

def parse(puzzle_input):
    """Parse text input"""
    
    return puzzle_input.strip()

def check_digest(data: str, append: str, check: str):
    """Calculate the hex digest of a plaintext value"""

    plain = data + append
    hash_value = md5(plain.encode('utf-8')).hexdigest()
    
    # if it starts with the check value
    if hash_value[:5] == check:
        return True, hash_value
    
    return False, -1

def part1(data):
    """Solve part 1"""

    append = 0
    password = ""

    while len(password) < 8:
        # check the digest value
        is_valid, digest = check_digest(data, str(append), '00000')
        if is_valid:
            # if it is, add the 6th char to the password
            password += digest[5]

        # move to the next append value
        append += 1

    return password

def part2(data):
    """Solve part 2"""

    append = 0
    password = [''] * 8

    while not all(password):
        # check the digest value
        is_valid, digest = check_digest(data, str(append), '00000')
        if is_valid:
            # ensure that the target index value is an integer
            if digest[5].isnumeric() and int(digest[5]) < 8:
                # ensure that location is empty
                if not password[int(digest[5])]:
                    # add the 6th char to the target location
                    password[int(digest[5])] = digest[6]

        # move to the next append value
        append += 1

    return ''.join(password)

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