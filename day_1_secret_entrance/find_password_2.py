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
def zero_passing_counter(codes: List[str]) -> int:
    """
    Determines how many times a lock passes by zero when making the turns given by codes

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
            # Big numbers need to get many passes added
            counts_to_add = abs(turn_amount // 100)

            # Something like 44 + L44 or 44 + L144
            if (position - turn_amount) % 100 == 0:
                counts_to_add += 1

            # Something like 55 + L60 or 55 + L160
            if position > 0 and (position - (turn_amount % 100)) < 0:
                counts_to_add += 1

            # Final modifications to state before next iteration
            zero_count += counts_to_add
            position = (position - turn_amount) % 100
            print(
                f"Adding {counts_to_add} due to a left turn of {turn_amount}. Count is now: {zero_count}. Dial is now at: {dial[position]}. Position is now: {position}."
            )

        elif direction == "R":
            # Big numbers need to get many passes added
            counts_to_add = abs(turn_amount // 100)

            # Something like 55 + R45 or 55 + R145
            if (position + turn_amount) % 100 == 0:
                counts_to_add += 1

            # Something like 55 + R65 or 55 + R165
            if (position + (turn_amount % 100)) > 100:
                counts_to_add += 1

            # Final modifications to state before next iteration
            zero_count += counts_to_add
            position = (position + turn_amount) % 100
            print(
                f"Adding {counts_to_add} due to a right turn of {turn_amount}. Count is now: {zero_count}. Dial is now at: {dial[position]}. Position is now: {position}."
            )

        else:
            # Just in case
            print(f"Direction is not L or R. It is: {direction}")

    # Return the count
    return zero_count


# Use the function to determine the password
password = zero_passing_counter(codes)
print(f"The password is: {password}")
