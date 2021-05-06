import pytest

from task import decompressRLElist


@pytest.mark.parametrize("a, expected_result", [([1, 2, 3, 4], [2, 4, 4, 4]),
                                                ([1, 1, 2, 3], [1, 3, 3])])
def test_decompressRLElist(a, expected_result):
    assert decompressRLElist(a) == expected_result
