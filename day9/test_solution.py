# test_solution.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture(name="data1")
def example1():
    """Parse the first example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.map_disk(puzzle_input)

@pytest.fixture(name="data2")
def example2():
    """Parse the second example input file and return that result"""
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(data1):
    """Test that input is parsed properly."""
    assert data1 == ['0','0','.','.','.','1','1','1','.','.','.','2','.','.',
                     '.','3','3','3','.','4','4','.','5','5','5','5','.','6',
                     '6','6','6','.','7','7','7','.','8','8','8','8','9','9']

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(data1):
    """Test part 1 on example input."""
    assert aoc.part1(data1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(data1):
    """Test part 2 on example input."""
    assert aoc.part2(data1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(data2):
    """Test part 2 on example input."""
    assert aoc.part2(data2) == ...
