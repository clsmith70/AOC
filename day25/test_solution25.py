# test_solution25.py

import pathlib
import pytest
import solution25 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""
    
    assert example1 == (4, 2)

def test_part1_example1(example1: list):
    """Test part 1 on example input."""
    
    assert aoc.part1(20151125, example1[0], example1[1]) == 32451966

def test_part2_example1(example1: list):
    """Test part 2 on example input."""
    
    assert aoc.part2() == "Power Cycle the machine and " \
         "have a Merry Christmas!"
