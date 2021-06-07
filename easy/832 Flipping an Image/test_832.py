import pytest

from task import flipAndInvertImage


@pytest.mark.parametrize("a, expected_result", [([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
                                                ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
                                                 [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])])
def test_flipAndInvertImage(a, expected_result):
    assert flipAndInvertImage(a) == expected_result
