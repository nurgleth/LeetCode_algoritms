import pytest

from task import createTargetArray


@pytest.mark.parametrize("a, b, expected_result", [([1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4]),
                                                   ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]),
                                                   ([1], [0], [1])])
def test_createTargetArray(a, b, expected_result):
    assert createTargetArray(a, b) == expected_result
