import pytest

from task import maxDepth


@pytest.mark.parametrize("a, expected_result", [("(1+(2*3)+((8)/4))+1", 3),
                                                ("(1)+((2))+(((3)))", 3),
                                                ("1+(2*3)/(2-1)", 1),
                                                ("1", 0)])
def test_maxDepth(a, expected_result):
    assert maxDepth(a) == expected_result
