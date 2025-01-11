# solution.py

import copy
import pathlib
import sys


def find_last_number(disk_map: list) -> int | None:
    # get the index of the last number in the map
    for i in range(len(disk_map) - 1, -1, -1):
        if isinstance(disk_map[i], int):
            return i
    return None


def map_disk(data: list) -> list:
    # map the sequence of files and free space
    disk_map = []
    file_id = 0

    # enumerate the list of files and free blocks
    for index, value in enumerate(data):
        # if index mod 2, this is a file
        if index % 2 == 0:
             # write the file_id value times
            for _ in range(int(value)):
                disk_map.append(file_id)
            file_id += 1
        # index not mod 2, this is free space
        else:
            # write '.' value times
            for _ in range(int(value)):
                disk_map.append('.')

    return disk_map


def get_contiguous_ranges(disk_map: list, item: int | str) -> list:
    # return the slices of contiguous free space on disk
    ranges = []
    start = None
    for index, value in enumerate(disk_map):
        if value == item:
            if start is None:
                start = index
        elif start is not None:
            ranges.append((start, index - 1))
            start = None
    if start is not None:
        ranges.append((start, len(disk_map) - 1))

    return ranges


def swap_blocks(disk_map: list, free_space: tuple, file_space: tuple) -> list:
    # swap the file and free space on disk
    file_size = file_space[1] - file_space[0] + 1
    file_id = disk_map[file_space[0]]
    for i in range(free_space[0], free_space[0] + file_size):
        disk_map[i] = file_id

    for j in range(file_space[0], file_space[1] + 1):
        disk_map[j] = '.'

    return disk_map

def calculate_filesystem_checksum(data: list) -> int:
    # accumulate the calculated checksum of each file block
    checksum = 0

    # loop over the entire file list
    for index in range(len(data)):
        # if the current index is not free space
        if isinstance(data[index], int):
            # accumulate the checksum at the current index
            checksum += int(data[index]) * index
        index += 1

    return checksum


def part1(disk_map: list) -> str:
    """Solve part 1"""
    # get the index of the first empty block
    left_index = disk_map.index('.')
    # get the index of the first file block from the end
    right_index = find_last_number(disk_map)

    # while the empty block index is less then the last file block index
    while left_index < right_index:
        # swap the file chunk with the free space
        disk_map[left_index], disk_map[right_index] = \
            disk_map[right_index], disk_map[left_index]
        # get new indices
        left_index = disk_map.index('.')
        right_index = find_last_number(disk_map)
    
    return f"Part 1: {calculate_filesystem_checksum(disk_map)}"


def part2(disk_map: list) -> str:
    """Solve part 2"""
    # get the highest file_id in the list
    highest_id = max([i for i in disk_map if i != '.'])
    # get the contiguous ranges of free space
    free_space = get_contiguous_ranges(disk_map, '.')

    while highest_id > 0:
        file_space = get_contiguous_ranges(disk_map, highest_id)
        file_size = file_space[0][1] - file_space[0][0] + 1
        for space in free_space:
            if (file_size <= (space[1] - space[0] + 1) and
                space[0] < file_space[0][0]):
                for i in range(space[0], space[0] + file_size):
                    disk_map[i] = highest_id
                for j in range(file_space[0][0], file_space[0][1] + 1):
                    disk_map[j] = '.'
                break
        highest_id -= 1
        # refresh the free space
        free_space = get_contiguous_ranges(disk_map, '.')

    # return the checksum
    return f"Part 2: {calculate_filesystem_checksum(disk_map)}"

def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = map_disk(data=puzzle_input)
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(copy.deepcopy(data))

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        raw_data = pathlib.Path(path).read_text(encoding='utf-8').strip()
        solutions = solve(puzzle_input=raw_data)
        print("\n".join(str(solution) for solution in solutions))