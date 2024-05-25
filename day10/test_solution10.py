# test_solution10.py

import pathlib
import pytest
import solution10 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        'value 5 goes to bot 2',
        'bot 2 gives low to bot 1 and high to bot 0',
        'value 3 goes to bot 1',
        'bot 1 gives low to output 1 and high to bot 0',
        'bot 0 gives low to output 2 and high to output 0',
        'value 2 goes to bot 2'
    ]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    solution1, outputs = aoc.part1(example1, [2, 5])
    product = outputs['output 0'][0] * outputs['output 1'][0] * \
        outputs['output 2'][0]
    
    assert solution1 == 'bot 2'
    assert product == 30
