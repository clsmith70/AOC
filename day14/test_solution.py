# test_solution.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture(name="data1")
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input), aoc.build_grid(11, 7)

def test_parse_example1(data1):
    """Test that input is parsed properly."""
    bots, grid = data1
    grid = aoc.place_bots(grid, bots)
    assert grid[0][3] == 2

def test_part1_example1(data1):
    """Test part 1 on example input."""
    bots, grid = data1
    grid = aoc.place_bots(grid, bots)
    assert aoc.part1(grid, bots) == "Part 1: 12"
