import pytest

from task import checkZeroOnes


@pytest.mark.parametrize("a, expected_result", [("111000", False),
                                                ("1101", True),
                                                ("110100010", False)])
def test_checkZeroOnes(a, expected_result):
    assert checkZeroOnes(a) == expected_result
