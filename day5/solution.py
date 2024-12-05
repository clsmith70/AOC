# solution.py

import pathlib
import sys

def parse(puzzle_input: str) -> tuple[list, list]:
    """Parse text input"""
    rules, pages = [], []
    # split the input into a list of two raw data strings
    data = list(puzzle_input.split('\n\n'))
    # parse the rules portion of the data
    rules = data[0].splitlines() # split into lines
    rules = [item.split('|') for item in rules] # split into pairs of strings
    rules = [(int(a), int(b)) for a, b in rules] # convert to tuples

    # parse the pages portion of the data
    pages = data[1].splitlines() # split into lines
    # convert each line to a list of integers
    pages = [[int(x) for x in item.split(',')] for item in pages]

    return rules, pages

def validate_pageset(pageset: list, rules: list) -> bool:
    """Check if a pageset is valid"""
    is_valid = False # assume that the pageset is not valid

    # loop over the rules
    for rule in rules:
        # if both rules are in the pageset
        if rule[0] in pageset and rule[1] in pageset:
            # and they are in the correct order, it is valid
            if pageset.index(rule[0]) < pageset.index(rule[1]):
                is_valid = True
            # otherwise, it is not; stop checking rules
            else:
                is_valid = False
                break
        # just one or none of the rule values in the pageset make it valid
        else:
            is_valid = True

    return is_valid

def reorder_invalid_pageset(pageset: list, rule: tuple):
    """Reorder invalid pageset to be valid"""
    # if both rule values are in the pageset
    if rule[0] in pageset and rule[1] in pageset:
        # and they are in the wrong order
        if pageset.index(rule[0]) > pageset.index(rule[1]):
            # swap them
            index1 = pageset.index(rule[0])
            index2 = pageset.index(rule[1])
            pageset[index1], pageset[index2] = pageset[index2], pageset[index1]
            return pageset
    return pageset

def part1(data: list):
    """Solve part 1"""
    middle_page_sum = 0

    rules, pagesets = data
    for pageset in pagesets:
        if validate_pageset(pageset, rules):
            middle_page_sum += pageset[len(pageset) // 2]

    return middle_page_sum

def part2(data: list):
    """Solve part 2"""
    middle_page_sum = 0

    rules, pagesets = data
    for pageset in pagesets:
        if not validate_pageset(pageset, rules):
            while True:
                for rule in rules:
                    pageset = reorder_invalid_pageset(pageset, rule)
                if validate_pageset(pageset, rules):
                    middle_page_sum += pageset[len(pageset) // 2]
                    break

    return middle_page_sum

def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input=puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))