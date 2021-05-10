import pytest

from task import checkIfPangram


@pytest.mark.parametrize("a, expected_result", [("thequickbrownfoxjumpsoverthelazydog", True),
                                                ("leetcode", False)])
def test_checkIfPangram(a, expected_result):
    assert checkIfPangram(a) == expected_result
