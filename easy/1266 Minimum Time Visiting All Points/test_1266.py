import pytest

from task import minTimeToVisitAllPoints, minTimeToVisitAllPoints1


@pytest.mark.parametrize("a, expected_result", [([[1, 1], [3, 4], [-1, 0]], 7),
                                                ([[3, 2], [-2, 2]], 5)])
def test_minTimeToVisitAllPoints(a, expected_result):
    assert minTimeToVisitAllPoints(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [([[1, 1], [3, 4], [-1, 0]], 7),
                                                ([[3, 2], [-2, 2]], 5)])
def test_minTimeToVisitAllPoints1(a, expected_result):
    assert minTimeToVisitAllPoints1(a) == expected_result
