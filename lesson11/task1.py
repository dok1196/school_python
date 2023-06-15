# -*- coding: utf-8 -*-
# Перейти на https://sbis.ru/
# Перейти в раздел Контакты
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Прячем длинные названия путей Xpath


# Открываем сайт sbis.ru
driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://sbis.ru/'
try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Неверно открыт сайт'
    # Находим и кликаем на ссылку "Контакты"
    contacts_link = driver.find_element(By.LINK_TEXT, 'Контакты')
    contacts_link.click()
    sleep(2)
    assert driver.find_element(By.CLASS_NAME, "sbisru-h2"), 'Открыта страница не "Контакты"'
    # Находим баннер Тензор и кликаем на него
    banner = driver.find_element(By.XPATH, '//*[@title="tensor.ru"]')
    banner.click()
    sleep(7)
    # Переключаемся на новую вкладку и проверяем, что находимся на сайте tensor.ru
    driver.switch_to.window(driver.window_handles[1])
    assert "tensor.ru" in driver.current_url,  'Url сайта не компании Тензор'
    # Находим блок новости "Сила в людях"
    element = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    news = driver.find_element(By.XPATH, '//*[contains(text(), "Нас 7 000 человек, мы — разные: ")]')
    assert news.is_displayed(),    'Блок новости "Сила в людях" не отображается'
    sleep(4)
    # Находим ссылку "Подробнее" в блоке новости "Сила в людях" и кликаем на нее
    links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Подробнее')]")
    # Выбираем ссылку с заданным порядковым номером
    link_index = 2
    link = links[link_index]
    link.click()
    # Проверяем, что открылась страница https://tensor.ru/about
    assert "https://tensor.ru/about" == driver.current_url
    sleep(3)
    # Закрываем браузер
finally:
    driver.quit()
