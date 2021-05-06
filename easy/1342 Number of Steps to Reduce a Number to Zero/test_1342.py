import pytest

from task import numberOfSteps


@pytest.mark.parametrize("a, expected_result", [(14, 6),
                                                (8, 4),
                                                (123, 12)])
def test_numberOfSteps(a, expected_result):
    assert numberOfSteps(a) == expected_result

