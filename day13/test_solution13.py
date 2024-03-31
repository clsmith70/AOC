# test_solution13.py

import pathlib
import pytest
import solution13 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    
    assert example1 == [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.'
        ]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    
    assert aoc.part1(example1) == 330

def test_part2_example1(example1):
    """Test part 2 on example input."""
    
    assert aoc.part2(example1) == 286
