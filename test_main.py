from typing import List
import pytest
from main import func2


def _generate_expected(inputs: List[int], operations: List[int]) -> List[int]:
    expected = []
    for op in operations:
        if op == 1:
            expected.append(sum(inputs))
        elif op == 2:
            expected.append(min(inputs))
        elif op == 3:
            expected.append(max(inputs))
        elif op == 4:
            expected.append(None)
    return expected


@pytest.mark.parametrize(
    ("inputs", "operations"),
    [([0, 5, 4], [1, 2, 3, 4])],
)
def test_func2_par(inputs: List[int], operations: List[int]):
    assert func2(inputs, operations) == _generate_expected(inputs, operations)


def test_func2():
    test_inputs = [1, 2, 3, 4]  # sum, min, max, quit
    data = [1, 2, 2, 3, 4, 5, 5, 6]
    expected = [sum(data), min(data), max(data), None]
    assert func2(data, test_inputs) == pytest.approx(expected)
