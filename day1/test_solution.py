# test_solution.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    """Parse the puzzle input and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example=example1):
    """Test that input is parsed properly."""
    assert example[0] == '3   4'

def test_part1_example1(example=example1):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 11

def test_part2_example1(example=example1):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 31
