from typing import List

# Read in the banks into a python list of strings
batteries_file_path = "batteries.txt"

banks = []

with open(batteries_file_path, "r") as batteries_file:
    for line in batteries_file:
        stripped_line = line.strip()
        if stripped_line:
            banks.append(stripped_line)

print(f"Total amount of banks: {len(banks)}")


# Create a function to find top 2 nums in a string
def find_top_2_nums(num_str: str):
    # Init top 2
    one = float("-inf")
    one_i = None

    two = float("-inf")
    two_i = None

    # Find largest number that isnt last, then find the largest number after that one

    # Iterate through characters in string
    for i, char in enumerate(num_str):
        num = int(char)

        # The case that num is equal to one and greater than two (must be index after one)
        if two_i:
            if num == one and two < one and i > one_i:
                two = num
                two_i = i

        # The case that num > one (must be not the last index)
        if num > one and i != (len(num_str) - 1):
            one = num
            one_i = i
            two = int(num_str[i + 1])
            two_i = i + 1

        # The case that num > one (but it is the last index)
        if num > one and i == (len(num_str) - 1):
            two = num
            two_i = i

        # The case that num > two and less than one (must be after one)
        if num > two and num < one and i > one_i:
            two = num
            two_i = i

    # Return final answer
    if one_i < two_i:
        return one, two


# Create a function to iterate through banks and add up total
def iter_banks(banks: List[str]):

    # Init total
    total = 0

    # Iter through banks and add top two to total
    for bank in banks:
        print(f"Processing bank: {bank}")
        one, two = find_top_2_nums(bank)
        print(f"Found top two: {one} + {two}")

        bank_total = int(str(one) + str(two))
        print(f"Adding: {bank_total}")
        total += bank_total

    # Return total
    return total

# Find total
total = iter_banks(banks)

# Print final result
print(f"Total joltage is: {total}.")
