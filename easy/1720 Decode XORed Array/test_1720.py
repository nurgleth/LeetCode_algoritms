import pytest

from task import decode


@pytest.mark.parametrize("a, b, expected_result", [([1, 2, 3], 1, [1, 0, 2, 1]),
                                                   ([6, 2, 7, 3], 4, [4, 2, 0, 7, 4])])
def test_decode(a, b, expected_result):
    assert decode(a, b) == expected_result
