# # # # my_list = [1, 2, 3, 4, 5]
# # # # for i in my_list:
# # # #     print(i)
# # # #     print(i+2)
# # # # for i in range(10): # Выведется список от 0 до 9, число 10 не включается
# # # #     print(i)
# # #
# # # # for i in range(3, 10): # Выведется список от 3 до 9, число 10 не включается
# # # #     print(i)
# # #
# # # # for i in range(3, 10, 2): # Выведется список от 3 до 9, с шагом 2 (3,5,7,9) число 10 не включается
# # # #     print(i)
# # #
# # # my_list = [11, 42, 63, 74, 15]
# # # for i in enumerate(my_list): # Получения кортежа где 1-ый индекск, 2-ой элемент списка
# # #     print(i)
# # import time
# #
# #
# # class Counter:
# #
# #     @staticmethod
# #     def get_current_time(self:
# #         return time.perf_counter()
# #
# #
# #     def __int__(self):
# #         self.start = self.get_current_time()
# #
# #
# #     def delta(self):
# #         return get_current_time() - self.start
# #
# # print(Counter.get_current_time())
# # c = Counter()
# # time = sleep()
# #
# #
# import math
# class Segment:
#     def __init__(self, p1, p2):
#         self.x1, self.y1 = p1
#         self.x2, self.y2 = p2
#
#     def length(self):
#         return round(math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2), 2)
#
#     def x_axis_intersection(self):
#         return self.y1 * self.y2 < 0
#
#     def y_axis_intersection(self):
#         return self.x1 * self.x2 <= 0
#
#
# data = [Segment((2, 3), (4, 5)).length,
#         Segment((1, 1), (1, 8)).length,
#         Segment((0, 0), (0, 1)).length,
#         Segment((15, 1), (18, 8)).length,
#         Segment((-2, -3), (4, 5)).x_axis_intersection,
#         Segment((-2, -3), (-4, -2)).x_axis_intersection,
#         Segment((0, -3), (4, 5)).x_axis_intersection,
#         Segment((-2, 3), (4, 5)).y_axis_intersection,
#         Segment((-2, -3), (4, 5)).y_axis_intersection,
#         Segment((-2, 3), (4, 0)).y_axis_intersection
#         ]
#
#
# test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]
#
# for i, d in enumerate(data):
#     assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
#     assert d() == test_data[i], assert_error
#     print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
# print('Всё ок')
# import unittest  # Не удалять
#
#
# # Здесь пишем код
#
#
# def treatment_sum(our_tuple):
#     """
#     Функция ловит исключения при помощи конструкции try/except
#     :param our_tuple: принимается кортеж
#     :return: получившийся результат
#     """
#     len_tuple = len(our_tuple)
#
#     if (len_tuple == 2 and type(our_tuple[0]) == type(our_tuple[1])):
#         return our_tuple[0] + our_tuple[1]
#
#     if (len_tuple == 2 and (type(our_tuple[0]) != int or type(our_tuple[1]) != int)):
#         try:
#             raise Exception('Нельзя сложить эти данные')
#         except Exception:
#             return 'Нельзя сложить эти данные'
#
#     if (len_tuple < 2):
#         try:
#             raise Exception('Недостаточно данных')
#         except Exception:
#             return ('Недостаточно данных')
#
#     if (len_tuple > 2):
#         raise Exception('Много данных')
#
#
# # Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
#
#
# class MyTestCase(unittest.TestCase):
#
#     def test(self):
#         data = [(3, 5), (3, '7'), (3,), (), ('23', '32')]
#
#         test_data = [8, 'Нельзя сложить эти данные', 'Недостаточно данных', 'Недостаточно данных', '2332']
#
#         for i, d in enumerate(data):
#             assert treatment_sum(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
#             print(f'Тестовый набор {d} прошёл проверку')
#
#         with self.assertRaises(Exception):
#             treatment_sum((3, 4, 5))
#         try:
#             treatment_sum((3, 4, 5))
#         except Exception as e:
#             assert e.args[0] == 'Много данных', 'Исключение имеет неправильный текст'
#         print('Всё ок')
#
#
# if __name__ == '__main__':
#     unittest.main()
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
#
# sbis_site = 'https://test.sbis.ru/'
# sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
# driver = webdriver.Chrome()
# try:
#     driver.get(sbis_site)
#     assert driver.current_url == sbis_site, 'Неверно открыт сайт'
#     assert driver.title == sbis_title, 'Не верный заголовок'
#     tabs = driver.find_elements(By.CSS_SELECTOR, 'sbisru-Header__menu-item')
#     # assert len(tabs) == 4, 'Должно быть 4 вкладки'
#
#     start_btn = driver.find_element(By.CSS_SELECTOR, 'sbisru-Button--primary')
#     start_btn_txt = 'Начать работу'
#     assert start_btn.text == start_btn_txt
#     assert start_btn.get_attribute('title') == start_btn_txt
#     assert start_btn.is_displayed()
#     start_btn.click()
# finally:
#     driver.quit()
#     context_menu = driver.find_element(By.CSS_SELECTOR, 'параметры элемента')

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# browser = webdriver.Chrome()
# sbis_site = 'https://sbis.ru/'
# try:
#     browser.get(sbis_site)
#     sleep(1)
#     assert browser.current_url == sbis_site, 'Неверно открыт сайт'
#     tabs = browser.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
#     assert len(tabs) == 4, "Должно быть 4 вкладки"
#
# finally:
#     browser.quit()



browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    tabs = browser.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, "Должно быть 4 вкладки"

finally:
    browser.quit()