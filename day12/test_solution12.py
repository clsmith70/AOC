# test_solution12.py

import json
import pathlib
import pytest
import solution12 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    with open(PUZZLE_DIR / "example1.txt", 'r') as accounting_file:
        puzzle_input = json.load(accounting_file)
    return puzzle_input

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {"e":[1,2,3],"f":{"a":2,"b":4},"g":[[[3]]],"h":{"a":{"b":4},"c":-1},"i":{"a":[-1,1]},"j":[-1,{"a":1}],"k":[],"l":{}}

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 18
