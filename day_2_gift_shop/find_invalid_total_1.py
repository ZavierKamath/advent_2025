from typing import Tuple, List

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
            if num_str[: ((length_of_num // 2))] == num_str[((length_of_num) // 2) :]:
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
