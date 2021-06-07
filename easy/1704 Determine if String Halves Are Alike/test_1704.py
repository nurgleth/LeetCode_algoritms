import pytest

from task import halvesAreAlike


@pytest.mark.parametrize("a, expected_result", [("book", True),
                                                ("textbook", False),
                                                ("MerryChristmas", False)])
def test_halvesAreAlike(a, expected_result):
    assert halvesAreAlike(a) == expected_result
