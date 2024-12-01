# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse text input"""
    return list(puzzle_input.split('\n'))

def make_lists(data: list) -> tuple[list, list]:
    """Create the two lists from the data input"""
    list1 = []
    list2 = []

    # loop over the lines of data and append the values to the lists
    for line in data:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

    return list1, list2

def part1(data):
    """Solve part 1"""
    distances = []
    list1, list2 = make_lists(data)

    # sort the lists
    list1 = sorted(list1)
    list2 = sorted(list2)

    if len(list1) == len(list2):
        # Get the distances between each pair of numbers
        for _, (value1, value2) in enumerate(zip(list1, list2)):
            distances.append(abs(value1 - value2))

    # return the sum of all distances
    return sum(distances)

def part2(data):
    """Solve part 2"""
    scores = []
    list1, list2 = make_lists(data)

    if len(list1) == len(list2):
        # Score the first list of numbers against the second list
        # Scoring is based on how many times a number from list 1 appears in
        # list2 multiplied by the number itself
        for value in list1:
            multiplier = list2.count(value)
            scores.append(value * multiplier)

    # return the sum of all scores
    return sum(scores)

def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=puzzle_data)
        print("\n".join(str(solution) for solution in solutions))
