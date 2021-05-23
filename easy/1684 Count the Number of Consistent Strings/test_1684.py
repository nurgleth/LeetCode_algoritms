import pytest

from task import countConsistentStrings


@pytest.mark.parametrize("a, b, expected_result", [("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
                         ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
                         ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4)])
def test_countConsistentStrings(a, b, expected_result):
    assert countConsistentStrings(a, b) == expected_result
