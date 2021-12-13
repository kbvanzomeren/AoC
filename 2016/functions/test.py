from functions import load_data

TEST_INPUT_DIR = "./inputs_test/"


def test(file_name, part1, part2, a1=1, a2=2, _load_data=None) -> None:
    test_file_path = TEST_INPUT_DIR + file_name
    if _load_data:
        data = _load_data(test_file_path)
    else:
        data = load_data(test_file_path)
    result_day_1 = part1(data)
    result_day_2 = part2(data)


    print(f"Answer to test part 1 is {result_day_1}")
    assert result_day_1 == a1

    print(f"Answer to test part 2 is {result_day_2}")
    assert result_day_2 == a2