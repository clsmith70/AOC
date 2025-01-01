# solution.py

import pathlib
import sys


def parse(puzzle_input: str):
    """Parse text input"""
    # make a list of the raw data
    temp = list(puzzle_input.split('\n'))
    # split each line into a list of strings
    temp = [line.split() for line in temp]
    # remove the colon from the first element in each line
    for line in temp:
        line[0] = line[0][:-1]
    # return a mapped list of integers
    return [list(map(int, line)) for line in temp]


def evaluate_equation(result: int, equation: list, pipe: bool = False):
    """Evaluate an equation and return the result"""
    answer = 0
    # create a blank set and a working set that starts with the first value
    # in the equation list
    new_set = []
    working_set = [equation[0]]
    # loop through the remaining equation values
    for index in range(1, len(equation)):
        # take the next value in the equation list
        next_int = equation[index]
        # add the sum and product of the next value with each value in the
        # working set
        for value in working_set:
            new_set.append(value + next_int)
            new_set.append(value * next_int)
            # if pipe is True, add the contatenated value and next value to
            # the new set
            if pipe: 
                new_set.append(int(str(value) + str(next_int)))
        # swap the sets and reset the new set
        working_set = new_set
        new_set = []
    # if the result we are looking for is in the working set, add it to the
    # answer variable
    if result in working_set:
        answer += result

    return answer


def part1(data: list):
    """Solve part 1"""
    total = 0
    # loop over each line and sum the evaluation of each equation
    for line in data:
        total += evaluate_equation(line[0], line[1:])
    return f"Part 1: {total}"

def part2(data: list):
    """Solve part 2"""
    total = 0
    # loop over each line and sum the evaluation of each equation
    # set pipe to True to use concatenation
    for line in data:
        total += evaluate_equation(line[0], line[1:], pipe=True)
    return f"Part 2: {total}"


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