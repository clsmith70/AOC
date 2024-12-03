# solution2.py

import copy
import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    # create an empty list
    puzzle_list = []
    # loop through the input, splitting each line into a list of integers
    for line in puzzle_input.split('\n'):
        puzzle_list.append([int(num) for num in line.split()])
    return puzzle_list

def report_is_safe(report: list) -> bool:
    """Check if a report is safe"""
    # start with a last_value of -1
    last_level = -1
    # start with a direction of 0: -1 == decreasing and 1 == increasing
    direction = 0

    # loop through the level values in the report, checking against the rules
    for level in report:
        # if the last level is -1, set it to the current level
        if last_level == -1:
            last_level = level
        else:
            if (level > last_level) and (level - last_level <= 3) and \
                (direction != -1):
                # if the current level is greater than the last level and the
                # change is less than or equal to 3, set the direction to 1
                direction = 1
            elif (level < last_level) and (last_level - level <= 3) and \
                (direction != 1):
                # if the current level is less than the last level and the
                # change is less than or equal to 3, set the direction to -1
                direction = -1
            else:
                return False
            last_level = level
    return True

def part1(data: list):
    """Solve part 1"""
    # Start counting safe reports
    safe_count = 0

    for report in data:
        # check if the report is safe
        # if so, add 1 to safe_count
        if report_is_safe(report):
            safe_count += 1

    return safe_count

def part2(data: list):
    """Solve part 2"""
    # Start counting safe reports
    safe_count = 0

    for report in data:
        # check if the report is safe
        # if so, add 1 to safe_count        
        if report_is_safe(report):
            safe_count += 1
        else:
            # check if removing one level makes the report safe
            # if so, add 1 to safe_count
            for i in range(len(report)):
                temp_report = copy.deepcopy(report)
                temp_report.pop(i)
                if report_is_safe(temp_report):
                    safe_count += 1
                    break

    return safe_count

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