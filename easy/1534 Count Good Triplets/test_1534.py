import pytest

from task import countGoodTriplets


@pytest.mark.parametrize("a, b, c, d, expected_result", [([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),
                                                         ([1, 1, 2, 2, 3], 0, 0, 1, 0)])
def test_countGoodTriplets(a, b, c, d, expected_result):
    assert countGoodTriplets(a, b, c, d) == expected_result
