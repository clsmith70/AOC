""" test_solution.py """

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture(name="data1")
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(data1):
    """Test that input is parsed properly."""
    assert data1[0][0] == ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.']
    assert data1[1] == (6, 4)

def test_part1_example1(data1):
    """Test part 1 on example input."""
    data, coords = data1
    assert aoc.part1(data=data, guard_coords=coords) == 'Part 1: 41'

def test_part2_example1(data1):
    """Test part 2 on example input."""
    data, coords = data1
    assert aoc.part2(data=data, guard_coords=coords) == 'Part2: 6'
