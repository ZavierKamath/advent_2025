from typing import List, Tuple

# Read in the banks into a python list of strings
batteries_file_path = "batteries.txt"

banks = []

with open(batteries_file_path, "r") as batteries_file:
    for line in batteries_file:
        stripped_line = line.strip()
        if stripped_line:
            banks.append(stripped_line)

print(f"Total amount of banks: {len(banks)}")


# Create a function to make m numbers after an index (i) go into a tuple
def mutate_top12(top12: List[int], top12_i: List[int], m: int, i: int, num_str: str):
    # Select m numbers after an index i of num_str
    if m > len(num_str[i:]):
        m = len(num_str[i:])

    num_slice = num_str[i : i + m]
    print(f"Slice being added: {num_slice}")
    num_slice_i = list(range(i, i + m))

    # Put them in the tuple
    insertion_start = len(top12) - m

    for j in range(m):
        # print(f"m is: {m}. Length of top12: {len(top12)}, index we are trying to access: {insertion_start + j}, num_slice: {num_slice}, index we are trying to access: {j}")
        top12[insertion_start + j] = num_slice[j]
        top12_i[insertion_start + j] = num_slice_i[j]

    # Return the tuple which has been modified
    return top12, top12_i


# Create a function to find top 12 nums in a string
def find_top_12_nums(num_str: str):
    # Init top 12
    top_12 = list(num_str[0:12])
    top_12_i = list(range(0, 12))
    print(f"Starting top 12: {top_12}")

    # Iterate through characters in string
    for i, char in enumerate(num_str):
        print(f"Processing: {char}")
        num = int(char)

        # If the length remaining is >= 12 and you find a number bigger than i=0
        length_remaining = len(num_str) - i - 1
        if (length_remaining >= 12) and (num > int(top_12[0])):

            print(f"12 or more remaining: {num} > {top_12[0]}")
            top_12, top_12_i = mutate_top12(top_12, top_12_i, 12, i, num_str)
            print(f"Top 12 is now: {top_12}")
            print(f"Top 12 i is now: {top_12_i}")

            continue

        # If the length remaining is something like 10 and you find a number bigger than i=2
        if i != 0:

            for length in range(min(max(length_remaining + 1, 1), 12), 0, -1):
                idx = 12 - length

                if (num > int(top_12[idx])) and (top_12_i[idx] < i):

                    print(f"{num} > {top_12[idx]} @ {idx}")
                    print(f"Length is: {length}")
                    top_12, top_12_i = mutate_top12(top_12, top_12_i, length, i, num_str)
                    print(f"Top 12 is now: {top_12}")
                    print(f"Top 12 i is now: {top_12_i}")

                    break

    return top_12


# Create a function to iterate through banks and add up total
def iter_banks(banks: List[str]):

    # Init total
    total = 0

    # Iter through banks and add top two to total
    for bank in banks:
        print(f"Processing bank: {bank}")
        top_12_nums = find_top_12_nums(bank)
        print(f"Found top twelve: {top_12_nums}")

        top_12_nums_str = ""
        for num in top_12_nums:
            top_12_nums_str += num

        bank_total = int(top_12_nums_str)
        print(f"Adding: {bank_total}")
        total += bank_total

    # Return total
    return total

# Find total
total = iter_banks(banks)

# Print final result
print(f"Total joltage is: {total}.")
