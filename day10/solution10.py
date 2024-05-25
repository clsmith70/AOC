# solution10.py

import pathlib
import re
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return list(puzzle_input.split('\n'))

def initialize(data: list, bots: dict, outputs: dict) -> None:
    """Initialize the bots and outputs"""

    botlist = set()
    outlist = set()

    for line in data:
        # find any bots in the line and add them to the set
        for bot in re.findall(r'bot \d+', line):
            botlist.add(bot)
        
        # find any outputs in the line and add them to the set
        for output in re.findall(r'output \d+', line):
            outlist.add(output)

    # sort the bots and add them to the robots dict with initial values
    for robot in sorted(botlist):
        bots[robot] = {"left": 0, "right": 0, 'ready': False}

    # sort the outputs and add them to the robots with an empty list
    for output in sorted(outlist):
        outputs[output] = []

def give_robot_chip(bot: str, value: int, robots: dict) -> None:
    """Give a robot a chip"""

    target_bot = robots[bot]
    if target_bot['right'] == 0:
        target_bot['right'] = value
    elif target_bot['left'] == 0:
        target_bot['left'] = value

    if target_bot['left'] > 0 and target_bot['right'] > 0:
        target_bot['ready'] = True

def pass_chip(source: str, side: str, dest: str, 
              robots: dict, outputs: dict) -> None:
    """Pass a chip between robots or from robot to output"""

    source_bot = robots[source]
    if dest.split()[0] == 'output':
        outputs[dest].append(source_bot[side])
        source_bot[side] = 0
    else:
        give_robot_chip(dest, source_bot[side], robots)
        source_bot[side] = 0

def part1(data: list, comparison: list) -> tuple[str, dict]:
    """Solve part 1"""

    bots = {}
    outputs = {}
    comp_bot = ''

    # initialize the bot and output dicts
    initialize(data, bots, outputs)

    while len(data) > 0:
        for line in data:
            # find all 'word #' strings in the line
            parts = re.findall(r'\w+ \d+', line)

            # if this is a value (parts has 2 elements)
            if len(parts) == 2:
                # give the value to the robot
                give_robot_chip(parts[1], int(parts[0].split()[1]), bots)
                data.pop(data.index(line))
            else:
                # bots are comparing and passing chips
                source, low, high = parts

                # if the source bot is ready
                if bots[source]['ready']:
                    # if this is our comparison bot, indicate it
                    if (bots[source]['left'] in comparison and
                        bots[source]['right'] in comparison):
                        comp_bot = source

                    # pass chips based on value comparisons
                    if bots[source]['left'] > bots[source]['right']:
                        pass_chip(source, 'left', high, bots, outputs)
                        pass_chip(source, 'right', low, bots, outputs)
                        data.pop(data.index(line))
                        bots[source]['ready'] = False
                    else:
                        pass_chip(source, 'right', high, bots, outputs)
                        pass_chip(source, 'left', low, bots, outputs)
                        data.pop(data.index(line))
                        bots[source]['ready'] = False

    return comp_bot, outputs

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1, outputs = part1(data=data, comparison=[17, 61])
    product = outputs['output 0'][0] * outputs['output 1'][0] * \
        outputs['output 2'][0]
    
    solution1 = f"Part 1: {solution1}"
    solution2 = f"Part 2: {product}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))