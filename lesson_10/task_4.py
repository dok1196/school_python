# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures('class_fixture')
class TestClass:
    def test_1(self):
        assert True

    def test_2_2(self, test_fixture):
        assert True

    @pytest.mark.usefixtures("test_fixture")
    def test_3_3(self):
        assert True
