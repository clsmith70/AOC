# test_aoc_template.py

import pathlib
import pytest
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    """Parse the second example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example=example1):
    """Test that input is parsed properly."""
    assert example == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example=example1):
    """Test part 1 on example input."""
    assert aoc.part1(example) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example=example1):
    """Test part 2 on example input."""
    assert aoc.part2(example) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example=example2):
    """Test part 2 on example input."""
    assert aoc.part2(example) == ...
