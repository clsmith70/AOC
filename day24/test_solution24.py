# test_solution24.py

import pathlib
import pytest
import solution24 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""
    
    assert example1 == [
        1, 2, 3, 4, 5,
        7, 8, 9, 10, 11
    ]

def test_part1_example1(example1: list):
    """Test part 1 on example input."""
    
    assert aoc.pack_sleigh(example1, 3) == 99

def test_part2_example1(example1: list):
    """Test part 2 on example input."""
    
    assert aoc.pack_sleigh(example1, 4) == 44
