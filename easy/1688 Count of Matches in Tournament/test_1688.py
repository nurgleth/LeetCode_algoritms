import pytest

from task import numberOfMatches


@pytest.mark.parametrize("a, expected_result", [(7, 6),
                                                (14, 13)])
def test_numberOfMatches(a, expected_result):
    assert numberOfMatches(a) == expected_result
