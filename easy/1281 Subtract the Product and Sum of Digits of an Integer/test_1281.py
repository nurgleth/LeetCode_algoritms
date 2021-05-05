import pytest

from task import subtractProductAndSum


@pytest.mark.parametrize("a, expected_result", [(234, 15),
                                                (4421, 21)])
def test_subtractProductAndSum(a, expected_result):
    assert subtractProductAndSum(a) == expected_result
