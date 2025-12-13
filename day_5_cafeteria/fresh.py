def parse_ingredients(ing_path: str):
    # Open the file and find the split
    with open(ing_path, 'r') as file:
        for i, line in enumerate(file):
            if line.strip() == '':
                split_line_idx = i
                print(f"Found empty line at: {i}")

    with open(ing_path, 'r') as file:
        # Find fresh ranges
        fresh_ranges = []
        for i, line in enumerate(file):
            if i == split_line_idx:
                break
            line = line.strip()
            id_range = line.split('-')
            fresh_ranges.append((int(id_range[0]), int(id_range[1])))

    with open(ing_path, 'r') as file:
        # Find spoiled ids
        spoiled_ids = []
        for i, line in enumerate(file):
            if i <= split_line_idx:
                continue
            spoiled_ids.append(int(line.strip()))

    # Return the two lists
    return fresh_ranges, spoiled_ids


def count_fresh(ing_path: str):
    # Read in the fresh ranges and spoiled ids lists
    print(f"Loading in ingredients: {ing_path}...")
    fresh_ranges, spoiled_ids = parse_ingredients(ing_path)
    print(f"Loaded. Length of fresh ranges: {
          len(fresh_ranges)}. Length of spoiled IDs: {len(spoiled_ids)}")

    # Iterate through spoiled ids and if it falls within a range, increment fresh count
    print("Finding available fresh IDs")
    total = 0
    for id in spoiled_ids:
        for id_range in fresh_ranges:
            if id_range[0] <= id <= id_range[1]:
                print(f"Available id: {id} falls within {
                      id_range[0]} - {id_range[1]}")
                total += 1
                print(f"Total is now: {total}")
                # Make sure to break so that we dont count multiple ranges
                break

    # Return total
    print(f"Found {total} available fresh ingredient IDs")
    return total


if __name__ == "__main__":
    total = count_fresh('ingredients.txt')
    print(f"Total fresh ingredient IDs: {total}")
    # Open the file and find the split
