from collections import defaultdict
from typing import List

# Find the longest contiguous integer in a column
# There will only be one space between the longest contiguous digit and the start of the next column


def handle(rows: List[str]):
    # Initialize grid
    grid = defaultdict(list)
    start = 0
    end = 4  # 4 is the longest possible contiguous integet
    should_end_next = False
    iteration = 1

    # Loop until end of string
    while True:
        print(f"Iteration: {iteration} | Looking from {start} - {end}")
        if should_end_next:
            break
        if end >= len(rows[0]):
            end = len(rows[0])
            should_end_next = True

        # Store the longest in each row
        longest = defaultdict(int)

        # Find longest contiguous number and save the index
        for i, row in enumerate(rows):
            for j, char in enumerate(row[start: end]):
                if char == ' ':
                    break  # At the end of longest or not longest
                if char.isdigit():
                    longest[i] += 1

        # Find the longest
        biggest_length = 0
        for row, length in longest.items():
            if length > biggest_length:
                biggest_length = length

        # Append the string slice to the proper row in the grid
        for i, row in enumerate(rows):
            grid[i].append(row[start: start + biggest_length])

        # Update start and end so next loop goes through the proper slice
        start += biggest_length + 1
        end = start + 4
        iteration += 1

    # Turn grid defaultdict into List[List[str]]
    new_grid = []
    for key, value in grid.items():
        new_grid.append(value)

    return new_grid


def read_into_grid(worksheet_path: str):
    rows = []
    with open(worksheet_path, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            rows.append(line)

    grid = handle(rows)

    return grid


def get_columns(grid):
    col_num = len(grid[0])
    row_num = len(grid)
    cols = defaultdict(list)
    for row in range(row_num):
        for col in range(col_num):
            cols[col].append(grid[row][col])

    final = []
    for key, value in cols.items():
        final.append(value)

    return final


def workout_column(column):
    print(f"PROCESSING COLUMN: {column}")
    rows = len(column)
    col_len = len(column[0])
    if column[-1].strip() == '+':
        total = 0
        for col in range(col_len):
            nums = []
            for i in range(0, rows - 1):
                num = column[i][col]
                if num != ' ':
                    nums.append(num)
                else:
                    continue
            num_to_add = int(('').join(nums))
            print(f"    - NUM TO ADD: {num_to_add}")
            total += num_to_add
    elif column[-1].strip() == '*':
        total = 1
        for col in range(col_len):
            nums = []
            for i in range(0, rows - 1):
                num = column[i][col]
                if num != ' ':
                    nums.append(num)
                else:
                    continue
            num_to_multiply = int(('').join(nums))
            print(f"    - NUM TO MULTIPLY: {num_to_multiply}")
            total *= num_to_multiply
    print(f"    - COLUMN TOTAL: {total}")
    return total


def compute_total(cols):
    total = 0
    for col in cols:
        col_tot = workout_column(col)
        total += col_tot
    return total


def main(worksheet_path):
    print("Starting main process")
    grid = read_into_grid(worksheet_path)
    print(f"Grid is: {grid}")
    columns = get_columns(grid)
    print(f"Columns are: {columns}")
    total = compute_total(columns)
    return total


if __name__ == '__main__':
    total = main('worksheet.txt')
    print(f"Total is: {total}")
