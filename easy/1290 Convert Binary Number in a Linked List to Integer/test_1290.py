import pytest

from task import getDecimalValue


@pytest.mark.parametrize("a, expected_result", [([1, 0, 1], 5),
                                                ([0], 0),
                                                ([1], 1),
                                                ([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 18880),
                                                ([0, 0], 0)])
def test_getDecimalValue(a, expected_result):
    assert getDecimalValue(a) == expected_result
