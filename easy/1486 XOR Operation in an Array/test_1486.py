import pytest

from task import xorOperation


@pytest.mark.parametrize("a, b, expected_result", [(5, 0, 8),
                                                   (4, 3, 8),
                                                   (1, 7, 7),
                                                   (10, 5, 2)])
def test_xorOperation(a, b, expected_result):
    assert xorOperation(a, b) == expected_result
