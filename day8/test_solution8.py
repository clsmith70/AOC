# test_solution8.py

import pathlib
import pytest
import solution8 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        'rect 3x2',
        'rotate column x=1 by 1',
        'rotate row y=0 by 4',
        'rotate column x=1 by 1'
    ]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    lit_pixels, screen = aoc.set_screen(example1, (3, 7))
    assert lit_pixels == 6
    assert screen == '.#..#.#\r\n#.#....\r\n.#.....'