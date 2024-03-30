# solution9.py

import pathlib
import sys
from itertools import permutations

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def add_location(source: str, destination: str, distance: int,
                 location_dict: dict) -> dict:
    """Add locations to the dictionary"""
    
    # if the source is already in the dict
    if source in location_dict.keys(): 
        # append the new values
        location_dict[source].append((destination, distance))
    else: 
        # otherwise, add it
        location_dict[source] = [(destination, distance)]

    # if the destination is already in the dict
    if destination in location_dict.keys(): 
        # append the new values
        location_dict[destination].append((source, distance))
    else: 
        # otherwise, add it
        location_dict[destination] = [(source, distance)]
    
def path_distance(path: tuple, location_dict: dict) -> int:
    """Return total cost of the path presented"""

    total = 0
    # make a list of the path tuple
    path = list(path)

    # while there are values in the path list
    while len(path) > 1:
        # pop the first one
        current = path.pop(0)
        # get the destinations for the current location
        destinations = location_dict[current]

        # for each distance / cost pair in destinations
        for (distance, cost) in destinations:
            # if the distance is equal to the path distance
            if distance == path[0]:
                # add it's cost to the total
                total += cost
                break

    return total

def part1(data: list) -> str:
    """Solve part 1"""

    location_dict = dict()
    shortest_distance = 999999999

    # for each line of data
    for line in data:
        # split the line and keep interesting data
        source, _, destination, _, distance = line.split()
        # add the location to the dict
        add_location(source, destination, int(distance), location_dict)
 
    # for each path in permutations of the dict keys
    for path in permutations(location_dict.keys()):
        # calculate the path distance
        trip = path_distance(path, location_dict)
        # if the trip is shorter than the shortest distance, save it
        if trip < shortest_distance:
            shortest_distance = trip

    return shortest_distance

def part2(data: list) -> str:
    """Solve part 2"""

    location_dict = dict()
    longest_distance = 0

    # for each line of data
    for line in data:
        # split the line and keep interesting data
        source, _, destination, _, distance = line.split()
        # add the location to the dict
        add_location(source, destination, int(distance), location_dict)
 
    # for each path in permutations of the dict keys
    for path in permutations(location_dict.keys()):
        # calculate the path distance
        trip = path_distance(path, location_dict)
        # if the trip is longer than the longest distance, save it
        if trip > longest_distance:
            longest_distance = trip

    return longest_distance


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