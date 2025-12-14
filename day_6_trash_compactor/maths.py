from collections import defaultdict

def read_into_grid(worksheet_path: str):
    grid = []
    with open(worksheet_path, 'r') as file:
        for line in file:
            line = line.split(' ')
            row = []
            for space in line:
                stripped_space = space.strip()
                if stripped_space != '':
                    row.append(stripped_space)
            grid.append(row)

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
    length = len(column)
    if column[-1] == '+':
        total = 0
        for i in range(0, length - 1):
            num = int(column[i])
            total += num
    elif column[-1] == '*':
        total = 1
        for i in range(0, length - 1):
            num = int(column[i])
            total *= num
    print(f"    - COLUMN TOTAL: {total}")
    return total

def compute_total(cols):
    total = 0
    for col in cols:
        col_tot = workout_column(col)
        total += col_tot
    return total

def main(worksheet_path):
    print(f"Starting main process")
    grid = read_into_grid(worksheet_path)
    print(f"Grid is: {grid}")
    columns = get_columns(grid)
    print(f"Columns are: {columns}")
    total = compute_total(columns)
    return total

if __name__ == '__main__':
    total = main('worksheet.txt')
    print(f"Total is: {total}")

