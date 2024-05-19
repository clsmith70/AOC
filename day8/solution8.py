# solution8.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def fill_top_left(x: int, y: int, screen: list) -> None:
    """Fill the top left area of the screen"""
    
    for i in range(y):
        for j in range(x):
            screen[i][j] = '#'

def shift_column(column: int, amount: int, screen: list) -> None:
    """Rotate a column by a specified amount"""

    for _ in range(amount):
        for r in range(len(screen) - 1, -1, -1):
            if r == len(screen) - 1:
                temp = screen[r][column]
                screen[r][column] = screen[r - 1][column]
            elif r == 0:
                screen[r][column] = temp
            else:
                screen[r][column] = screen[r - 1][column]         

def shift_row(row: int, amount: int, screen: list) -> None:
    """Rotate a row by a specified amount"""
    
    for _ in range(amount):
        elem = screen[row].pop(-1)
        screen[row].insert(0, elem)

def display(screen: list) -> str:
    """Display a line of the screen"""

    display_line = ""
    for row in screen:
        for pixel in row:
            display_line += pixel if pixel != '' else ' '
        display_line += '\r\n'

    return display_line

def set_screen(data: str, screen_size: tuple = (6, 50)) -> str:
    """Solve part 1"""

    rows, columns = screen_size
    screen = [['' for _ in range(columns)] for _ in range(rows)]

    for line in data:
        if 'rect' in line:
            x, y = line.split()[1].split('x')
            fill_top_left(int(x), int(y), screen)
        elif 'rotate' in line:
            _, elem, addr, _, shift = line.split()
            index = int(addr.split('=')[-1])

            if elem == 'row':
                shift_row(index, int(shift), screen)
            elif elem == 'column':
                shift_column(index, int(shift), screen)

    lit_pixels = sum([len(list(filter(bool, line))) for line in screen])
    finished_screen = display(screen)

    return lit_pixels, finished_screen

def solve(puzzle_input):
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {set_screen(data=data)[0]}"
    solution2 = f"Part 2: \n{set_screen(data=data)[1]}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))