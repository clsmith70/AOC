# solution.py
# answers - P1: 778, P2: 1925
import pathlib
import sys

def parse(puzzle_input: str):
    """Parse text input"""
    return [list(map(int, line)) for line in puzzle_input.split('\n')]


def map_locations(data: list) -> dict:
    map = {}
    for row in range(len(data)):
        for col in range(len(data[0])):
            map[(row, col)] = data[row][col]

    return map


def map_neighbors(area_map: dict) -> dict:
    neighbors = {}
    for key in area_map.keys():
        i, j = key
        neighbors[key] = {(i-1, j), (i+1, j), (i, j-1), (i, j+1)} & \
            area_map.keys()

    return neighbors


def part1(data: list):
    """Solve part 1"""
    area_map = map_locations(data)
    neighbors = map_neighbors(area_map)
    paths = lambda s: [s] if area_map[s] == 9 else \
        sum([paths(n) for n in neighbors[s] \
             if area_map[n] == area_map[s] + 1], [])  # noqa: E731

    return f"Part 1: {sum(len(set(paths(c))) for 
                        c in area_map if area_map[c] == 0)}"


def part2(data: list):
    """Solve part 2"""
    area_map = map_locations(data)
    neighbors = map_neighbors(area_map)
    paths = lambda s: [s] if area_map[s] == 9 else \
        sum([paths(n) for n in neighbors[s] \
             if area_map[n] == area_map[s] + 1], [])  # noqa: E731

    return f"Part 2: {sum(len(paths(c)) for 
                        c in area_map if area_map[c] == 0)}"


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