import pytest

from task import subsetXORSum, subsetXORSum1


@pytest.mark.parametrize("a, expected_result", [([1, 3], 6),
                                                ([5, 1, 6], 28),
                                                ([3, 4, 5, 6, 7, 8], 480)])
def test_subsetXORSum(a, expected_result):
    assert subsetXORSum(a) == expected_result

def test_subsetXORSum1(a, expected_result):
    assert subsetXORSum(a) == expected_result
