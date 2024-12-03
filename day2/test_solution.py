# test_solution.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture(name="data")
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(data):
    """Test that input is parsed properly."""
    assert data[0] == [7, 6, 4, 2, 1]

def test_part1_example1(data):
    """Test part 1 on example input."""
    assert aoc.part1(data) == 2

def test_part2_example1(data):
    """Test part 2 on example input."""
    assert aoc.part2(data) == 4
