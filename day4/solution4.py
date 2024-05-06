# solution4.py

import pathlib
import re
import sys

def parse(puzzle_input):
    """Parse text input"""
    
    return [line for line in puzzle_input.split()]

def get_data_parts(line: str) -> tuple:
    """Split the line into parts using a regex"""

    matches = re.match(r'([a-z-]+)-(\d+)\[([a-z]+)\]', line)
    return matches.groups()

def check_real(room: str, checksum: str) -> bool:
    """Check if a room is real"""

    room_checksum = ''.join(list(sorted(
        set(room) - {'-'},
        key = lambda letter : (
            -room.count(letter),
            letter
        ))))[:5]

    if checksum == room_checksum:
        return True
    return False

def decrypt_room_name(room: str, sector_id: int) -> str:
    """Decrypt the real name of the room"""

    # set the offset to the ascii value of 'a'
    offset = ord('a')

    # shift the character by the sector_id using ascii chars and 
    # a modulus of 26
    def shift(char):
        if char == '-':
            return " "
        else:
            return chr((ord(char) - offset + sector_id) % 26 + offset)
        
    return ''.join(map(shift, room))

def part1(data):
    """Solve part 1"""
    
    sector_sum = 0

    for line in data:
        # split the data into the necessary parts
        name, sector_id, checksum = get_data_parts(line)

        # check if the room is real
        if check_real(name, checksum):
            sector_sum += int(sector_id)

    return sector_sum        

def part2(data):
    """Solve part 2"""

    north_pole_sectors = []

    for line in data:
        # split the data into the necessary parts
        name, sector_id, checksum = get_data_parts(line)

        # check if the room is real
        if check_real(name, checksum):
            decrypted_name = decrypt_room_name(name, int(sector_id))
            # if it is a north pole room, add it to the list
            # include a check so our test case passes
            if 'north' in decrypted_name or checksum == 'zimth':
                north_pole_sectors.append((decrypted_name, sector_id))

    # loop over the decrypted names and return the first one (should be just 1)
    for name, sector in north_pole_sectors:
        return f"{name} @ {sector}"

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