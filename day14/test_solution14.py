# test_solution14.py

import pathlib
import pytest
import solution14 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""
    
    assert example1 == [
    'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
    'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
    ]

def test_part1_example1(example1: list):
    """Test part 1 on example input."""

    assert aoc.part1(example1, 1000) == ('Comet', 1120)

def test_part2_example1(example1: list):
    """Test part 2 on example input."""

    assert aoc.part2(example1, 1000) == ('Dancer', 689)
