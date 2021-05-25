import pytest

from task import sortSentence, sortSentence1


@pytest.mark.parametrize("a, expected_result", [("is2 sentence4 This1 a3", "This is a sentence"),
                                                ("Myself2 Me1 I4 and3", "Me Myself and I")])
def test_sortSentence(a, expected_result):
    assert sortSentence(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [("is2 sentence4 This1 a3", "This is a sentence"),
                                                ("Myself2 Me1 I4 and3", "Me Myself and I")])
def test_sortSentence1(a, expected_result):
    assert sortSentence1(a) == expected_result
