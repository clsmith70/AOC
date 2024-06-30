# test_aoc_template.py

import pathlib
import pytest
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    """Fixture for example 1 input file"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    """Fixture for example 2 input file"""
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
