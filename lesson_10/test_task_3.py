# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('args, expected_result', [
    pytest.param((10, 2), 5),
    pytest.param((100, 10, 2, 5), 1),
    pytest.param((1, 1, 1, 1, 1), 1.0, marks=pytest.mark.smoke),
    pytest.param((-30, 2), -15, marks=pytest.mark.skip(reason='division by negative number')),
])
def test_all_division(args, expected_result):
    assert all_division(*args) == expected_result
