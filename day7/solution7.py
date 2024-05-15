# solution7.py

import pathlib
import re
import regex
import sys

def parse(puzzle_input):
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def separate_address(address: str) -> tuple:
    """Separate the addresses into supernets and hypernets"""

    # get all net types from the address
    allnets = re.split(r'\[|\]', address)
    # get all the hypernets from the address (enclosed in square brackets)
    hypernets = re.findall(r'\[(.*?)\]', address)

    # capture all the supernets (outside of square brackets)
    supernets = []
    for net in allnets:
        if net not in hypernets:
            supernets.append(net)

    return supernets, hypernets

def part1(data: str) -> bool:
    """Solve part 1"""

    # compile a regex to look for palindromic pairs like [abba]
    regex = re.compile(r'([a-z])((?!\1)[a-z])\2\1')

    # get the address parts
    supernets, hypernets = separate_address(data)

    # find all supernets with palindrome pairs
    # where the hypernet has none
    if (any([regex.search(s) for s in supernets]) and
        not any([regex.search(h) for h in hypernets])):
        return True

    return False

def part2(data: str) -> bool:
    """Solve part 2"""

    # create regex to look for a 3 character set like [aba]
    aba_regex = r"(\w)(\w)\1"

    # get the address parts
    supernets, hypernets = separate_address(data)

    # find all possible matches
    aba_matches = []
    for s in supernets:
        overlaps = regex.findall(aba_regex, s, overlapped=True)
        if overlaps:
            aba_matches += overlaps

    # look for bab in each hypernet
    for h in hypernets:
        for aba in aba_matches:
            bab = aba[1] + aba[0] + aba[1]
            if bab in h:
                return True

    return False

def solve(puzzle_input):
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {sum(part1(ip) for ip in data)}"
    solution2 = f"Part 2: {sum(part2(ip) for ip in data)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))