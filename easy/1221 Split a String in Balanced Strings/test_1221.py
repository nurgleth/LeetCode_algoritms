import pytest

from task import balancedStringSplit


@pytest.mark.parametrize("a, expected_result", [("RLRRLLRLRL", 4),
                                                ("RLLLLRRRLR", 3),
                                                ("LLLLRRRR", 1),
                                                ("RLRRRLLRLL", 2)])
def test_balancedStringSplit(a, expected_result):
    assert balancedStringSplit(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [("RLRRLLRLRL", 4),
                                                ("RLLLLRRRLR", 3),
                                                ("LLLLRRRR", 1),
                                                ("RLRRRLLRLL", 2)])
def test_balancedStringSplit1(a, expected_result):
    assert balancedStringSplit(a) == expected_result
