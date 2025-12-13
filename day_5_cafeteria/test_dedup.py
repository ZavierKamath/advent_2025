from total import dedup

if __name__ == '__main__':
    test_ranges = [
        (3, 5),
        (5, 6),
        (6, 99)
    ]

    deduped_ranges = dedup(test_ranges)
    print(f"Deduped ranges:")
    for id_range in list(deduped_ranges):
        print(id_range)

