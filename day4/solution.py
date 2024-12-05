# solution.py

import pathlib
import sys

def parse(puzzle_input: str):
    """Parse text input"""
    return list(puzzle_input.split('\n'))

def is_valid(x, y, x_size, y_size) -> bool:
    """Check if the given coordinates are valid"""
    return 0 <= x < x_size and 0 <= y < y_size

def search_word_in_direction(grid, n, m, word, index, x, y, x_dir, y_dir):
    """Searches for the given word in the given direction"""
    if index == len(word):
        return True

    if is_valid(x, y, n, m) and word[index] == grid[x][y]:
        return search_word_in_direction(grid, n, m, word, index + 1,
            x + x_dir, y + y_dir, x_dir, y_dir)

    return False

def search_word(grid, word):
    """Counts the number of occurrences of the given word in the grid"""
    word_count = 0
    lines = len(grid)
    columns = len(grid[0])

    # The 8 possible directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(lines):
        for j in range(columns):
            # check for a match to the first letter in the word
            if grid[i][j] == word[0]:
                for x_dir, y_dir in directions:
                    if search_word_in_direction(grid, lines, columns, word, 0,
                        i, j, x_dir, y_dir):
                        word_count += 1

    return word_count

def search_mas(x_coord, y_coord, grid):
    """Searches for X-MAS from the 'A' position in the grid"""
    # The 4 corners
    top_left = grid[x_coord - 1][y_coord - 1]
    top_right = grid[x_coord + 1][y_coord - 1]
    bottom_left = grid[x_coord - 1][y_coord + 1]
    bottom_right = grid[x_coord + 1][y_coord + 1]

    # Check from 'A' to the 4 corners to see if MAS is in an X shape
    # either forward or reverse
    if (top_left == 'M' and top_right == 'M' and 
        bottom_left == 'S' and bottom_right == 'S'):
        return True
    elif (top_left == 'M' and top_right == 'S' and
        bottom_left == 'M' and bottom_right == 'S'):
        return True
    elif (top_left == 'S' and top_right == 'M' and
        bottom_left == 'S' and bottom_right == 'M'):
        return True
    elif (top_left == 'S' and top_right == 'S' and
        bottom_left == 'M' and bottom_right == 'M'):
        return True
    else:
        return False

def part1(data: list):
    """Solve part 1"""
    return search_word(data, "XMAS")

def part2(data: list):
    """Solve part 2"""
    x_mas_count = 0

    # Loop through the data omitting the edges looking for MAS in an X shape
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == 'A':
                if search_mas(i, j, data):
                    x_mas_count += 1

    return x_mas_count

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