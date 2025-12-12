import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def get_map(map_path: str):
    # Initialize an array to store row arrays in
    map = []

    # Read in the file and append rows as lists
    with open(map_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_list = list(line.strip())
            map.append(line_list)

    # Return the map
    return map

def get_validity(x: int, y: int, map: List[List[str]], rows: int, cols: int):
    # Define adjacent direction list
    adjacent_directions = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (-1, 0),
        (0, -1)
    ]

    if map[y][x] != '@':
        return False

    # Find adjacent directions to toilet paper roll
    is_valid = False
    count = 0
    for direction in adjacent_directions:
        new_x = x + direction[0]
        new_y = y + direction[1]

        # If adjacent space is paper roll
        if (-1 < new_x < cols) and (-1 < new_y < rows):
            if (map[new_y][new_x] == '@'):
                
                # Find paper rolls adjacent to space
                count += 1

    if count < 4:
        is_valid = True

    # Return validity
    return is_valid

def compute_adj(map: List[List[str]], rows: int, cols: int):
    count = 0
    adj = []
    for row in range(0, rows):
        adj_row = []
        for col in range(0, cols):
            valid = get_validity(col, row, map, rows, cols)
            if valid:
                count += 1
                adj_row.append('x')
            else:
                if map[row][col] == '.':
                    adj_row.append('.')
                else:
                    adj_row.append('@')
        adj.append(adj_row)

    return adj, count

def print_map(map: List[List[str]]):
    for row in map:
        print(''.join(row))

def get_available_rolls(map: List[List[str]], rows: int, cols: int):
    # Count valid spaces
    logging.info('Creating adjacent map...')
    adj, count = compute_adj(map, rows, cols)

    # Print out map with valid rolls
    print_map(adj)

    return adj, count

def create_new_map(adj: List[List[str]], rows: int, cols: int):
    # Iterate and replace x with .
    new_map = []
    for row in range(rows):
        new_row = []
        for col in range(cols):
            if adj[row][col] == '.' or adj[row][col] == 'x':
                new_row.append('.')
            else:
                new_row.append('@')
        new_map.append(new_row)

    # Return the new map
    return new_map

def clear_rolls(map_path: str):
    logging.info('Started application')

    # Load the map
    logging.info('Loading map...')
    map = get_map(map_path)
    rows, cols = len(map), len(map[0])
    logging.info(f"Map shape: {rows} x {cols}")
    print_map(map)

    # Get map of available rolls and count
    total = 0
    iters = 1
    while True:
        logging.info(f"Iteration of clearing: {iters}")
        adj, count = get_available_rolls(map, rows, cols)
        total += count
        logging.info(f"Adding {count} to total. Total is now: {total}")
            
        # Exit condition is if clearing returns zero
        if count < 1: 
            logging.info(f"Breaking out due to zero available rolls")
            break

        # Make new map by replacing x with .
        map = create_new_map(adj, rows, cols)
        iters += 1

    logging.info(f"Final total is: {total}")
    return total

if __name__ == '__main__':
    total = clear_rolls('map.txt')
    logging.info(f"Script finished running. Total was: {total}")
