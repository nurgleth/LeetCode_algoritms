import pytest

from task import removeOuterParentheses


@pytest.mark.parametrize("a, expected_result", [("(()())(())", "()()()"),
                                                ("(()())(())(()(()))", "()()()()(())"),
                                                "()()", ""])
def test_removeOuterParentheses(a, expected_result):
    assert removeOuterParentheses(a) == expected_result
