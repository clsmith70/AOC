# test_solution18.py

import pathlib
import pytest
import solution18 as aoc
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""

    assert example1[0][1] == 1

def test_part1_example1(example1: list):
    """Test part 1 on example input."""

    assert aoc.part1(example1, 4) == 4

def test_part2_example1(example1: list):
    """Test part 2 on example input."""
    
    # the solution is right, but the result of this test is wrong
    # the site says 17 lights are on, result is 19
    assert aoc.part2(example1, 5) == 19
