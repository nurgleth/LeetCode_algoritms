import pytest

from task import uniqueMorseRepresentations


@pytest.mark.parametrize("a, expected_result", [(["gin", "zen", "gig", "msg"],
                                                 2)])
def test_uniqueMorseRepresentations(a, expected_result):
    assert uniqueMorseRepresentations(a) == expected_result
