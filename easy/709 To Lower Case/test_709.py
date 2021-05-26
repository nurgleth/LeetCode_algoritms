import pytest

from task import toLowerCase


@pytest.mark.parametrize("a, expected_result", [("Hello", "hello"),
                                                ("here", "here"),
                                                ("LOVELY", "lovely")])
def test_toLowerCase(a, expected_result):
    assert toLowerCase(a) == expected_result
