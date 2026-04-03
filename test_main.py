from main import func2


def test_func2():
    test_inputs = [1, 2, 3, 4]  # sum, min, max, quit
    data = [1, 2, 2, 3, 4, 5, 5, 6]
    expected = [sum(data), min(data), max(data), None]
    assert func2(data, test_inputs) == expected
