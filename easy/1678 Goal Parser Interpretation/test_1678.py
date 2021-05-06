import pytest

from task import interpret, interpret1


@pytest.mark.parametrize("a, expected_result", [("G()(al)", "Goal"),
                                                ("G()()()()(al)", "Gooooal"),
                                                ("(al)G(al)()()G", "alGalooG")])
def test_interpret(a, expected_result):
    assert interpret(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [("G()(al)", "Goal"),
                                                ("G()()()()(al)", "Gooooal"),
                                                ("(al)G(al)()()G", "alGalooG")])
def test_interpret1(a, expected_result):
    assert interpret1(a) == expected_result
