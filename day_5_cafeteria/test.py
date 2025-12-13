from total import count_fresh

if __name__ == '__main__':
    test_path = 'test_ingredients_2.txt'
    total = count_fresh(test_path)
    print(f"Found test total: {total}")
