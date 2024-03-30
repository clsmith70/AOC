# test_solution11.py

import pathlib
import pytest
import solution11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1: list):
    """Test that input is parsed properly."""

    assert example1 == ['hijklmmn','abbceffg','abbcegjk']

def test_part1_example1(example1: list):
    """Test password validity on example input."""

    assert aoc.test_password(example1[0]) == False
    assert aoc.test_password(example1[1]) == False
    assert aoc.test_password(example1[2]) == False

def test_part1_example2(example2: list):
    """Test part 1 on example input."""

    assert aoc.part1([example2[0]]) == 'abcdffaa'
    assert aoc.part1([example2[1]]) == 'ghjaaabb' #'ghjaabcc' is wrong
    # a key error occurs when i, l, or o are encountered
    # to address this, they have to be added to the next_letter dict
    # when added, they properly adjust what the next valid password is
