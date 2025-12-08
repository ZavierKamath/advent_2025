from typing import List

# Read in the codes into a python list of strings
codes_file_path = "codes.txt"

codes = []

with open(codes_file_path, "r") as codes_file:
    for line in codes_file:
        stripped_line = line.strip()
        if stripped_line:
            codes.append(stripped_line)

print(f"The number of turns in codes is: {len(codes)}")


# Define the algorithm for determining the amount of times we land on zero
def zero_landing_counter(codes: List[str]) -> int:
    """
    Determines how many times a lock lands on zero when making the turns given by codes

    Args:
        codes: list of string rotations

    Returns:
        number of times the lock lands on zero
    """
    # Initialize start position and zero count
    start = 50
    position = start
    zero_count = 0

    dial = range(0, 100)

    # Iterate through codes and determine new position
    for turn in codes:
        # turn is something like 'L3' or 'R56'
        direction = turn[0]
        turn_amount = int(turn.replace("L", "").replace("R", ""))
        if direction == "L":
            position = (position - turn_amount) % 100
            print(f"Turning left by {turn_amount}. Dial is now at {dial[position]}")
        elif direction == "R":
            position = (position + turn_amount) % 100
            print(f"Turning right by {turn_amount}. Dial is now at {dial[position]}")
        else:
            print(f"Direction is not L or R. It is: {direction}")
        if dial[position] == 0:
            zero_count += 1
            print(f"Found a zero occurance. Count is now: {zero_count}")

    # Return the count
    return zero_count


# Use the function to determine the password
password = zero_landing_counter(codes)
print(f"The password is: {password}")
