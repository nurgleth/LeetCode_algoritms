import pytest

from task import truncateSentence


@pytest.mark.parametrize("a, b, expected_result", [("Hello how are you Contestant", 4, "Hello how are you"),
                                                   ("What is the solution to this problem", 4, "What is the solution"),
                                                   ("chopper is not a tanuki", 5, "chopper is not a tanuki")])
def test_truncateSentence(a, b, expected_result):
    assert truncateSentence(a, b) == expected_result
