# test_solution.py

import pathlib
import pytest
from collections import defaultdict
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture(name="data1")
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(data1):
    """Test that input is parsed properly."""
    test_out = defaultdict(int)
    test_out[125] = 1
    test_out[17] = 1
    assert data1 == test_out
def test_part1_example1(data1):
    """Test part 1 on example input."""
    assert aoc.part1(data1) == "Part 1: 55312"

def test_part2_example1(data1):
    """Test part 2 on example input."""
    assert aoc.part2(data1) == "Part 2: 65601038650482"
