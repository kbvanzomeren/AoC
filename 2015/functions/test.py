from functions import load_data

TEST_INPUT_DIR = "./inputs_test/"


def test(file_name, part1, part2=None, a1=1, a2=2, _load_data=None, _load_kwargs={}, data=None) -> None:
    test_file_path = TEST_INPUT_DIR + file_name
    if data:
        pass
    elif _load_data:
        data = _load_data(test_file_path, **_load_kwargs)
    else:
        data = load_data(test_file_path)
    result_day_1 = part1(data)

    print(f"Answer to test part 1 is {result_day_1}")
    # print(f"Solution is correct = {result_day_1 == a1}")

    if part2:
        result_day_2 = part2(data)
        print(f"Answer to test part 2 is {result_day_2}")
        # print(f"Solution is correct = {result_day_2 == a2}")
