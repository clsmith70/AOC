# test_aoc_template.py

import pathlib
import pytest
import solution7 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ['123 -> x','456 -> y','x AND y -> d','x OR y -> e','x LSHIFT 2 -> f','y RSHIFT 2 -> g','NOT x -> h','NOT y -> i']

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1, outgate='d') == 72

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1, ingate='x', ingate_value=72, outgate='d') == 72