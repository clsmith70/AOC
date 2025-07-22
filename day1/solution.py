# solution.py - AOC 2017, day 1


def read_file(infile: str) -> list:
    with open(infile, 'r') as f:
        return list(map(int, f.readline().strip()))
    

def inverse_captcha(line: list) -> int:
    length = len(line)
    total = 0

    for i in range(length):
        if i < length - 1 and line[i] == line[i + 1]:
            total += line[i]
        elif i == length - 1 and data[0] == data[i]:
            total += data[i]

    return total


def half_round(line: list) -> int:
    length = len(line)
    half_length = length // 2
    total = 0

    for i in range(length):
        if i < half_length and data[i] == data[i + half_length]:
            total += data[i]
        elif i >= half_length and data[i] == data[i - half_length]:
            total += data[i]

    return total


if __name__ == '__main__':
    data = read_file('input.txt')

    print(f"Part 1: {inverse_captcha(data)}")
    print(f"Part 2: {half_round(data)}")
