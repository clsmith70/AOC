# test_solution16.py

import pathlib
import pytest
import solution16 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""
    
    assert example1[0] == 'Sue 1: goldfish: 9, cars: 0, samoyeds: 9'

def test_part1_example1(example1: list):
    """Test part 1 on example input."""

    test_ticker = {'children': 3, 'cats': 4, 'samoyeds': 2, 'pomeranians': 3,
          'akitas': 2, 'vizslas': 0, 'goldfish': 10, 'trees': 3,
          'cars': 2, 'perfumes': 9}
    assert aoc.part1(example1, test_ticker) == 4

def test_part2_example1(example1: list):
    """Test part 2 on example input."""

    test_ticker = {'children': 3, 'cats': 1, 'samoyeds': 2, 'pomeranians': 3,
          'akitas': 2, 'vizslas': 0, 'goldfish': 10, 'trees': 3,
          'cars': 2, 'perfumes': 9}    
    assert aoc.part2(example1, test_ticker) == 3