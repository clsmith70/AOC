# test_solution7.py

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
    assert example1[-1] == 'ioxxoj[asdfgh]zxcvbn'

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert sum(aoc.part1(ip) for ip in example1) == 2

def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert sum(aoc.part2(ip) for ip in example2) == 3
