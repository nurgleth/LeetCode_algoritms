import pytest

from task import replaceDigits, replaceDigits1


@pytest.mark.parametrize("a, expected_result", [("a1c1e1", "abcdef"),
                                                ("a1b2c3d4e", "abbdcfdhe")])
def test_replaceDigits(a, expected_result):
    assert replaceDigits(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [("a1c1e1", "abcdef"),
                                                ("a1b2c3d4e", "abbdcfdhe")])
def test_replaceDigits1(a, expected_result):
    assert replaceDigits1(a) == expected_result
