import pytest

from task import sumOddLengthSubarrays


@pytest.mark.parametrize("a, expected_result", [([1, 4, 2, 5, 3], 58),
                                                ([1, 2], 3)])
def test_sumOddLengthSubarrays(a, expected_result):
    assert sumOddLengthSubarrays(a) == expected_result
