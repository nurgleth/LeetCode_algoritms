import pytest

from task import interpret


@pytest.mark.parametrize("a, expected_result", [("G()(al)", "Goal"),
                                                ("G()()()()(al)", "Gooooal"),
                                                ("(al)G(al)()()G", "alGalooG")])
def test_interpret(a, expected_result):
    assert interpret(a) == expected_result
