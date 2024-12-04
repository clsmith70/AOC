# test_solution.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture(name="data1")
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture(name="data2")
def example2():
    """Parse the second example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(data1):
    """Test that input is parsed properly."""
    assert data1 == ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']

def test_part1_example1(data1):
    """Test part 1 on example input."""
    assert aoc.part1(data1) == 161

def test_part2_example2(data2):
    """Test part 2 on example input."""
    assert aoc.part2(data2) == 48
