import pytest

from task import countMatches


@pytest.mark.parametrize("a, b, c, expected_result",
                         [([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                           "color", "silver", 1),
                          ([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                           "type", "phone", 2)])
def test_countMatches(a, b, c, expected_result):
    assert countMatches(a, b, c) == expected_result
