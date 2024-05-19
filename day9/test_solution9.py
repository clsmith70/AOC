# test_solution9.py

import pathlib
import pytest
import solution9 as aoc

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
    assert example1 == [
        'ADVENT',
        'A(1x5)BC',
        '(3x3)XYZ',
        'A(2x2)BCD(2x2)EFG',
        '(6x1)(1x3)A',
        'X(8x2)(3x3)ABCY'
    ]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 57

def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 242394
