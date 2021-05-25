import pytest

from task import sortSentence


@pytest.mark.parametrize("a, expected_result", [("is2 sentence4 This1 a3", "This is a sentence"),
                                                ("Myself2 Me1 I4 and3", "Me Myself and I")])
def test_sortSentence(a, expected_result):
    assert sortSentence(a) == expected_result
