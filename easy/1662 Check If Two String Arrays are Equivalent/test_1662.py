import pytest

from task import arrayStringsAreEqual, arrayStringsAreEqual1


@pytest.mark.parametrize("a, b, expected_result", [(["ab", "c"], ["a", "bc"], True),
                                                   (["a", "cb"], ["ab", "c"], False),
                                                   (["abc", "d", "defg"], ["abcddefg"], True)])
def test_arrayStringsAreEqual(a, b, expected_result):
    assert arrayStringsAreEqual(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [(["ab", "c"], ["a", "bc"], True),
                                                   (["a", "cb"], ["ab", "c"], False),
                                                   (["abc", "d", "defg"], ["abcddefg"], True)])
def test_arrayStringsAreEqual1(a, b, expected_result):
    assert arrayStringsAreEqual1(a, b) == expected_result
