""" solution.py for day 6 """

import copy
import pathlib
import sys

def parse(puzzle_input: str):
    """Parse text input"""
    puzzle_list = list(puzzle_input.splitlines())
    # create a list of each row
    for item in puzzle_list:
        puzzle_list[puzzle_list.index(item)] = list(item)
    # get the starting coordinate of the guard
    guard_coord = (0, 0)
    # loop over the rows, searching for the guard
    for row in puzzle_list:
        if '^' in row:
            # save the row and index of the guard
            guard_coord = (puzzle_list.index(row), row.index('^'))
    # return the puzzle data list and starting coordinates of the guard
    return puzzle_list, guard_coord


def get_blockable_coordinates(data: list) -> list:
    """Get a list of all blockable coordinates in the area"""
    coordinates = []
    for rindex, row in enumerate(data):
        for cindex, col in enumerate(row):
            if col == '.':
                coordinates.append((rindex, cindex))
    return coordinates


def get_next_move(guard_coordinates: tuple, guard_symbol: str) -> tuple:
    """Get the next coordinates and possible symbol for the guard"""
    match guard_symbol:
        case '^':
            return guard_coordinates[0] - 1, guard_coordinates[1], '>'
        case '>':
            return guard_coordinates[0], guard_coordinates[1] + 1, 'v'
        case 'v':
            return guard_coordinates[0] + 1, guard_coordinates[1], '<'
        case '<':
            return guard_coordinates[0], guard_coordinates[1] - 1, '^'
        case _:
            return guard_coordinates[0], guard_coordinates[1], guard_symbol
        

def check_guard_on_map(area: list, guard_coordinates: tuple) -> bool:
    """Check if the guard's current coordinates are still in the area"""
    return (guard_coordinates[0] >= 0 and 
            guard_coordinates[0] <= len(area) and
            guard_coordinates[1] >= 0 and
            guard_coordinates[1] <= len(area[0])
    )


def add_visited(guard_coordinates: tuple, visited_locations: list):
    """Add the visited location if it is not already in the list"""
    if guard_coordinates not in visited_locations:
        visited_locations.append(guard_coordinates)


def check_for_obstacle(obstacle: list, coordinates: tuple, area: list) -> bool:
    """Check the given coordinates for any obstacles"""
    return any([(c in area[coordinates[0]][coordinates[1]]) for c in obstacle])


def move_guard(guard_coords: tuple, area: list) -> tuple[tuple, bool]:
    """Move the guard to the next location or change the guard's direction"""
    # get the current guard symbol
    guard = area[guard_coords[0]][guard_coords[1]]
    # get the next location and new symbol for the guard
    # if the path is blocked, the new guard symbol is used
    # if the path is not blocked, the next coordinates are used
    next_x, next_y, new_guard_symbol = get_next_move(guard_coords, guard)
    on_map = check_guard_on_map(area, guard_coords)
    try:
        blocked = check_for_obstacle(['#', 'O'], (next_x, next_y), area)
    except IndexError:
        on_map = False

    if on_map and blocked:
        # turn the guard 90 degrees to the right
        area[guard_coords[0]][guard_coords[1]] = new_guard_symbol
        return guard_coords, on_map
    elif on_map and not blocked:
        # move the guard one step forward
        area[next_x][next_y] = guard
        return (next_x, next_y), on_map
    else:
        return guard_coords, on_map


def part1(data: list, guard_coords: tuple) -> str:
    """Solve part 1"""
    visited_locations = [guard_coords]
    on_map = True

    # copy the map
    area = copy.deepcopy(data)

    while on_map:
        guard_coords, on_map = move_guard(guard_coords, area)
        add_visited(guard_coords, visited_locations)

    return f"Part 1: {len(visited_locations)}"


def part2(data: list, guard_coords: tuple) -> str:
    """Solve part 2"""
    # count the obstacles in the area and set the maximum number of loops
    obstacles = sum([row.count('#') for row in data])
    max_loops = (len(data) * len(data[0]) - (obstacles + 1)) * 4

    # keep a list of obstacle coordinates that resulted in the guard
    # being stuck in a loop
    loop_positions = []

    # get blockable coordinates and remove the position of the guard
    # and the position directly in front of the guard
    blockable_coords = get_blockable_coordinates(data)

    for coord in blockable_coords:
        # get a copy of the data to work with
        area = copy.deepcopy(data)
        guard = guard_coords
        # indicate the guard is on them map
        on_map = True
        # place an obstacle at this coordinate
        area[coord[0]][coord[1]] = 'O'

        # move the guard until the loop count reaches the maximum
        # or the guard is no longer on the map
        loop_count = 0
        while on_map and loop_count < max_loops:
            guard, on_map = move_guard(guard, area)
            loop_count += 1

        if on_map and loop_count >= max_loops:
            loop_positions.append((coord[0], coord[1]))

    return f"Part 2: {len(loop_positions)}"


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data, coords = parse(puzzle_input=puzzle_input)
    solution1 = part1(data=data.copy(), guard_coords=coords)
    solution2 = part2(data=data.copy(), guard_coords=coords)

    return solution1, solution2


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))
