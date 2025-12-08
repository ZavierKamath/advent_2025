from typing import Tuple, List
import math

ranges_file_path = "id_ranges.txt"

ranges = []

with open(ranges_file_path, "r") as ranges_file:
    # Read in the ranges file
    ranges_content = ranges_file.read()

    # Split and iterate through the string
    ranges_strings_list = ranges_content.split(",")
    for num_range in ranges_strings_list:

        start = int(num_range.split("-")[0])
        end = int(num_range.split("-")[1])

        range_tuple = (start, end)
        ranges.append(range_tuple)


# Create a function to find all divisors of a number
def find_divisors(n: int):
    divisors = set()
    # Iterate from 1 up to the square root of n (inclusive)
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    # Convert the set to a sorted list
    return sorted(list(divisors))


# Create a function to determine if a number has repeat pattern
def determine_if_pattern(num: str):
    # Find possible divisors of length of num
    length_of_num = len(num)
    divisors = find_divisors(length_of_num)

    # Iterate through divisors and split the number up into segments
    for divisor in divisors:
        # Cover bad case
        if divisor > length_of_num // 2:
            continue

        # Find segments
        unique = set()
        for i in range(0, length_of_num, divisor):
            segment = num[i : i + divisor]
            unique.add(segment)

        # If segment has more than 1 entry, it's bad
        if len(unique) < 2:
            return True

    return False


# Create a function that can find duplex numbers
def find_duplex_nums(ranges: Tuple[int, int]):
    # Initialize a list to return all duplex numbers
    duplex_numbers = []

    # Iterate through ranges and append duplex numbers
    for num_range in ranges:
        print(f"Processing range: {num_range}")

        # Iterate through numbers in range
        for num in range(num_range[0], num_range[1] + 1):
            num_str = str(num)
            length_of_num = len(num_str)

            # If first half and second half of number string are equal
            if determine_if_pattern(num_str):
                duplex_numbers.append(num)
                print(f"Duplex identified: {num}")

    return duplex_numbers


# Define a function that finds total
def find_duplex_total(duplex_numbers: List[str]):
    # Iterate through duplex numbers and add up total
    total = 0
    for num in duplex_numbers:
        total += num

    return total


# Find duplex nums
duplex_nums = find_duplex_nums(ranges)

# Find total
total = find_duplex_total(duplex_nums)

# Print result
print(f"Duplex total is: {total}")
