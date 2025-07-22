# solution.py - AOC 2017, day 2


def find_divisible_numbers(numbers: list) -> list:
    """
    Finds the two numbers in a list that are evenly divisible
    numbers is a list of integers

    Returns a tuple of the one found pair
    """
    found_pair = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] != numbers[j]:
                num1 = numbers[i]
                num2 = numbers[j]

                # check the divisibility in both directions
                if (num1 % num2 == 0) or (num2 % num1 == 0):
                    if found_pair is not None:
                        return None
                    else:
                        found_pair = (num1, num2)

    return found_pair    



if __name__ == '__main__':
    # Read input data
    rawdata = open('input.txt', 'r')

    # Process rows into lists of integers
    data = []
    for line in rawdata:
        data.append([int(i) for i in line.split('\t')])

    # Calculate the checksum for each row
    rowsums = []
    for line in data:
        maximum = max(line)
        minimum = min(line)
        rowsums.append(maximum - minimum)

    # Write part 1 output    
    print(f"Part 1: {sum(rowsums)}")

    # TODO: Find the two evenly divisible numbers on each row
    quotients = []
    for line in data:
        divisible_numbers = find_divisible_numbers(line)
        a, b = sorted(divisible_numbers, reverse=True)
        quotients.append(a // b)

    # TODO: Return the sum of the quotients
    print(f"Part 2: {sum(quotients)}")
