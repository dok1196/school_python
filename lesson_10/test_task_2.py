# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты


import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(4, 0, 2)


@pytest.mark.smoke
def test1():
    assert all_division(10, 2) == 5, 'Неверный результат деления двух чисел'

@pytest.mark.acceptance
def test2():
    assert all_division(100, 10, 2, 5) == 1, 'Неверный результат деления трех чисел'

@pytest.mark.acceptance
def test3():
    assert all_division(1, 1, 1, 1, 1) == 1.0, 'Неверный результат деления числа на самого себя'


@pytest.mark.acceptance
def test4():
    assert all_division(-30, 2) == -15, 'Неверный результат деления отрицательного числа на положительное число'
