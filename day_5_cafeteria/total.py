from typing import List, Tuple

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


def find_unincapsulated(deduped):
    incapsulated = set()
    for idx_1, id_range_1 in enumerate(deduped):
        for idx_2, id_range_2 in enumerate(deduped):
            if idx_1 == idx_2:
                continue

            if id_range_1[0] >= id_range_2[0] and id_range_1[1] <= id_range_2[1]:
                incapsulated.add(id_range_1)

    print(f"Found incapsulated: {incapsulated}")
    unincapsulated = deduped - incapsulated
    return unincapsulated


def deduplication_conditionals(ranges: List[Tuple[int]]):
    deduped = set()
    not_needed = set()
    did_add = False
    for idx_1, id_range_1 in enumerate(ranges):
        print(f"PROCESSING: {id_range_1}")

        # Look at the other ranges
        for idx_2, id_range_2 in enumerate(ranges):
            if idx_1 == idx_2: 
                continue

            print(f"    - matching with: {id_range_2}")

        # (3, 5) (4, 6)
            # Case 1: something like 1 = (10, 15) and 2 = (13, 18) create new (10, 18)
            if (id_range_1[1] <= id_range_2[1]) and (id_range_1[1] >= id_range_2[0]):

                # Optional case where 1 = (10, 15) and 2 = (9, 18)
                if id_range_2[0] <= id_range_1[0]:
                    new_range = (id_range_2[0], id_range_2[1])
                # Case 1
                else:
                    new_range = (id_range_1[0], id_range_2[1])

                # Add this deduped range
                print(f"        - case 1: found {new_range}")
                if id_range_1 != new_range:
                    not_needed.add(id_range_1)
                if id_range_2 != new_range:
                    not_needed.add(id_range_2)
                deduped.add(new_range)
                did_add = True

            # Case 2: something like 1 = (10, 15) and 2 = (5, 12) create new (5, 15)
            elif id_range_1[1] >= id_range_2[1] and id_range_2[1] >= id_range_1[0]:

                # Optional case where 1 = (4, 15) and 2 = (5, 12)
                if id_range_1[0] <= id_range_2[0]:
                    new_range = (id_range_1[0], id_range_1[1])

                # Case 2
                else:
                    new_range = (id_range_2[0], id_range_1[1])

                # Add this deduped range
                print(f"        - case 2: found {new_range}")
                if id_range_1 != new_range:
                    not_needed.add(id_range_1)
                if id_range_2 != new_range:
                    not_needed.add(id_range_2)
                deduped.add(new_range)
                did_add = True

            # Case 3: two totally separate ranges
            else:
                if id_range_1 not in deduped:
                    print(f"        - case 3: adding {id_range_1}")
                    deduped.add(id_range_1)
                if id_range_2 not in deduped:
                    print(f"        - case 3: adding {id_range_2}")
                    deduped.add(id_range_2)

    deduped = deduped - not_needed

    return deduped, did_add


def dedup(ranges: List[Tuple[int]]):
    # Continue going until there's nothing left to add to deduped
    first = True
    iteration = 1
    while True:

        # For each range
        print(f"Doing iteration: {iteration}")
        if first:
            deduped, did_add = deduplication_conditionals(ranges)
                    
            # No longer first
            first = False
        else:
            deduped, did_add = deduplication_conditionals(deduped)
        iteration += 1
        print(f"deduped is now: {deduped}\n")

        # If nothing was added, return
        if not did_add:
            print(f"Found nothing new. Breaking")
            break


    # Return deduped ranges
    print(f"Before unincapsulating: {deduped}")
    deduped = find_unincapsulated(deduped)
    print(f"After unincapsulating: {deduped}")
    return deduped


def count_from_range(deduped):
    total = 0
    for id_range in deduped:
        diff = id_range[1] - id_range[0] + 1
        total += diff
    return total


def count_fresh(ing_path: str):
    # Read in the fresh ranges and spoiled ids lists
    print(f"Loading in ingredients: {ing_path}...")
    fresh_ranges, spoiled_ids = parse_ingredients(ing_path)
    print(f"Loaded. Length of fresh ranges: {
          len(fresh_ranges)}. Length of spoiled IDs: {len(spoiled_ids)}")

    # Iterate through spoiled ids and if it falls within a range, increment fresh count
    print("Finding available fresh IDs")
    deduped_ranges = dedup(fresh_ranges)

    # Find count from ranges
    total = count_from_range(deduped_ranges)
    print(f"Found {total} fresh ingredient IDs")
    return total


if __name__ == "__main__":
    total = count_fresh('ingredients.txt')
    print(f"Total fresh ingredient IDs: {total}")
    # Open the file and find the split
