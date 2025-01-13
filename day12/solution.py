# solution.py

import pathlib
import sys

def parse(puzzle_input: str) -> dict:
    """Parse text input"""
    # set up a dictionary
    data = {}
    raw = puzzle_input.split('\n')
    rows, columns = len(raw), len(raw[0])

    for row in range(rows):
        for col in range(columns):
            data[(col, row)] = raw[row][col]

    return data


def define_area(grid: dict, ycoord: int, xcoord: int) -> tuple[set, int, int]:
    """Define the region, perimeter, and area counts"""
    diffs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    region = set()
    area, perimeter = 0, 0
    border = [(ycoord, xcoord)]

    while border:
        y, x = border.pop()
        if (y, x) in region:
            continue
        region.add((y, x))
        area += 1

        for diffy, diffx in diffs:
            newy, newx = y + diffy, x + diffx
            if grid.get((newy, newx)) == grid[y, x]:
                border.append((newy, newx))
            else:
                perimeter += 1

    return region, perimeter, area


def get_fences(region: set) -> int:
    """Count the number of fence segments around the given plots"""
    corners, double = set(), 0
    xset, yset = set(x for y,x in region), set(y for y,x in region)
    
    for y in range(min(yset), max(yset) + 2):
        for x in range(min(xset), max(xset) + 2):
            index = sum(((y + dy,x + dx) in region) * sf
                        for dx, dy, sf in [(-1, -1, 1), (-1, 0, 2),
                                (0, -1, 4), (0, 0, 8)])
            if index not in [0, 3, 5, 10, 12, 15]:
                corners.add((y, x))
            if index in [6, 9]:
                double += 1

    return len(corners) + double


def part1(grid: list):
    """Solve part 1"""
    seen = set()
    fences = 0
    for (y, x) in grid:
        if (y, x) not in seen:
            region, perimeter, area = define_area(grid, y, x)
            seen.update(region)
            fences += area * perimeter
    return f"Part 1: {fences}"


def part2(grid: list):
    """Solve part 2"""
    seen = set()
    fences = 0
    for (y, x) in grid:
        if (y, x) not in seen:
            region, perimeter, area = define_area(grid, y, x)
            seen.update(region)
            fences += area * get_fences(region)
    return f"Part 2: {fences}"


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