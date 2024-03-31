# solution13.py

import pathlib
import sys
from itertools import permutations

def parse(puzzle_input: str) -> list:
    """Parse text input"""

    return [line for line in puzzle_input.split('\n')]

def build_guest_list(data: list, guest_list: dict) -> dict:
    """Build the guest list from the descriptions"""

    for line in data:
        # pull out interesting data about each guest
        guest, _, position, score, *_, neighbor = line.split()
        # remove the ending period
        neighbor = neighbor[:-1]
        # if this would be a loss, convert to a negative int
        if position == 'lose':
            score = -int(score)
        # if this would be a gain, convert to a positive int
        elif position == 'gain':
            score = int(score)

        # if the guest already exists in the dict
        # append the new record data
        # otherwise create a record for them
        if guest in guest_list.keys():
            guest_list[guest].append((neighbor, score))
        else:
            guest_list[guest] = [(neighbor, score)]

    return guest_list

def get_neighbor(guest_list: dict, person: str) -> tuple:
    """Get the neighbors to the left and right of the current person"""

    # get this persons position in the dict
    position = guest_list.index(person)

    # if they are at the beginning, get the second and last guests
    # if they are in the middle, get the guests before and after
    # if they are at the end, get the one before the the first guest
    if position == 0:
        return (guest_list[position + 1], guest_list[-1])
    elif position == len(guest_list) - 1:
        return (guest_list[position - 1], guest_list[0])
    else:
        return (guest_list[position - 1], guest_list[position + 1])

def get_score(guest_list: dict, person: str, neighbor: str) -> int:
    """Get the score relative to two guests in the dict"""

    # get the current guest
    current_guest = guest_list[person]

    # loop through their positions relative to other guests
    # if this record is the other half of the pairing, return the score
    for (nextTo, score) in current_guest:
        if nextTo == neighbor:
            return score

def get_happiness(permutation, guest_list: dict) -> int:
    """Calculate the happiness of the current seating arrangement"""

    happiness = 0

    # loop through this arrangement
    # get the score for the left and right neighbors
    for p in permutation:
        (a, b) = get_neighbor(list(permutation), p)
        happiness += get_score(guest_list, p, a)
        happiness += get_score(guest_list, p, b)

    return happiness

def add_host(guest_list: dict) -> dict:
    """Add the party host to the list"""

    # the host has no gain or loss in happiness
    # no matter where they sit
    for key in guest_list.keys():
        guest_list[key].append(('Host', 0))
    
    guest_list['Host'] = []
    for key in guest_list.keys():
        guest_list['Host'].append((key, 0))

    return guest_list

def part1(data: list) -> str:
    """Solve part 1"""
    
    guest_list = dict()
    maximum_happiness = 0

    # build the guest list and get all possible arrangements
    guest_list = build_guest_list(data, guest_list)
    arrangements = permutations(guest_list.keys())

    # loop over each arrangement group and calculate happiness score
    for group in arrangements:
        group_happiness = get_happiness(group, guest_list)
        if group_happiness > maximum_happiness:
            maximum_happiness = group_happiness

    return maximum_happiness

def part2(data: list) -> str:
    """Solve part 2"""

    guest_list = dict()
    maximum_happiness = 0

    # build the guest list and add the host
    guest_list = build_guest_list(data, guest_list)
    guest_list = add_host(guest_list)
    # get all possible arrangements
    arrangements = permutations(guest_list.keys())

    # loop over each arrangement group and calculate hapiness score
    for group in arrangements:
        group_happiness = get_happiness(group, guest_list)
        if group_happiness > maximum_happiness:
            maximum_happiness = group_happiness

    return maximum_happiness

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