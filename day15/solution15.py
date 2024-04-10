# solution15.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def get_ingredients(data: list, ingredients: list) -> dict:
    """Get ingredient properties from raw data"""

    for line in data:
        # split on : to get the name and remainder of the line
        _, rest = line.split(': ')
        # create a list of the remaining items
        # values: capacity, durability, flavor, texture, calories
        rest = [int(a.split()[1]) for a in rest.split(',')]
        ingredients.append(rest)

def score_cookie(data: list) -> tuple:
    """Calculate recipe scores and return the highest score"""
    highest_score, best_500_cal = 0, 0
    ingredients = list()
    get_ingredients(data, ingredients)

    if len(ingredients) == 4:
        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - i - j):
                    l = 100 - i - j -k
                    score = 0

                    capacity = ingredients[0][0] * i + \
                        ingredients[1][0] * j + \
                        ingredients[2][0] * k + \
                        ingredients[3][0] * l
                    durability = ingredients[0][1] * i + \
                        ingredients[1][1] * j + \
                        ingredients[2][1] * k + \
                        ingredients[3][1] * l
                    flavor = ingredients[0][2] * i + \
                        ingredients[1][2] * j + \
                        ingredients[2][2] * k + \
                        ingredients[3][2] * l
                    texture = ingredients[0][3] * i + \
                        ingredients[1][3] * j + \
                        ingredients[2][3] * k + \
                        ingredients[3][3] * l
                    calories = ingredients[0][4] * i + \
                        ingredients[1][4] * j + \
                        ingredients[2][4] * k + \
                        ingredients[3][4] * l
                    
                    if (capacity <= 0 or durability <= 0 or
                        flavor <= 0 or texture <= 0):
                        # score = 0
                        continue
                    
                    score = capacity * durability * flavor * texture
                    
                    if score > highest_score:
                        highest_score = score
                    
                    if calories == 500 and score > best_500_cal:
                        best_500_cal = score
                    
    elif len(ingredients) == 2:
        for i in range(101):
            for j in range(101 - i):
                score = 0

                capacity = ingredients[0][0] * i + \
                    ingredients[1][0] * j
                durability = ingredients[0][1] * i + \
                    ingredients[1][1] * j
                flavor = ingredients[0][2] * i + \
                    ingredients[1][2] * j
                texture = ingredients[0][3] * i + \
                    ingredients[1][3] * j
                calories = ingredients[0][4] * i + \
                    ingredients[1][4] * j
                
                if (capacity <= 0 or durability <= 0 or
                    flavor <= 0 or texture <= 0):
                    # score = 0
                    continue
                
                score = capacity * durability * flavor * texture
                
                if score > highest_score:
                    highest_score = score
                
                if calories == 500 and score > best_500_cal:
                    best_500_cal = score

    return highest_score, best_500_cal

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    s1, s2 = score_cookie(data)
    solution1 = f"Part 1: {s1}"
    solution2 = f"Part 2: {s2}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))