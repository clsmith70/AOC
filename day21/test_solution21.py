# test_solution21.py

import pathlib
import pytest
import solution21 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""
    
    assert example1 == [
        'Hit Points: 12',
        'Damage: 7',
        'Armor: 2'
    ]

def test_part1_example1(example1: list):
    """Test part 1 on example input."""
    
    assert aoc.fight(example1) == (8, 0)
