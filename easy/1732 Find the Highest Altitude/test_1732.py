import pytest

from task import largestAltitude


@pytest.mark.parametrize("a, expected_result", [([-5, 1, 5, 0, -7], 1),
                                                ([-4, -3, -2, -1, 4, 3, 2], 0)])
def test_largestAltitude(a, expected_result):
    assert largestAltitude(a) == expected_result
