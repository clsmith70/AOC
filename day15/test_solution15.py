# test_solution15.py

import pathlib
import pytest
import solution15 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""

    assert example1 == [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ]

def test_ingredients_example1(example1: list):
    """Test that the ingredient list is properly created."""

    ingredients = list()
    aoc.get_ingredients(example1, ingredients)
    assert ingredients == [
        [-1, -2, 6, 3, 8],
        [2, 3, -2, -1, 3]
    ]

def test_soutions_example1(example1: list):
    """Test part 1 on example input."""
    # when test values calculate correctly, puzzle answers are wrong
    p1, p2 = aoc.score_cookie(example1)
    assert p1 == 62842880
    assert p2 == 57600000
