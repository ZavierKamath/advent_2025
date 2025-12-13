from total import find_unincapsulated

if __name__ == '__main__':
    test = [
        (3, 5),
        (10, 20),
        (12, 18),
    ]
    test = set(test)

    unincap = find_unincapsulated(test)
    print(unincap)
