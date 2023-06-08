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

# Открываем сайт sbis.ru
browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    browser.get(sbis_site)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    # Находим и кликаем на ссылку "Контакты"
    contacts_link = browser.find_element(By.LINK_TEXT, 'Контакты')
    contacts_link.click()
    sleep(4)
    assert browser.find_element(By.CLASS_NAME, "sbisru-h2"), 'Открыта страница не "Контакты"'
    # # Находим баннер Тензор и кликаем на него
    # tensor_banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Тензор']")))
    # tensor_banner.click()
    #
    # # Переключаемся на новую вкладку
    # driver.switch_to.window(driver.window_handles[1])
    #
    # # Проверяем, что находимся на сайте tensor.ru
    # assert "tensor.ru" in driver.current_url
    #
    # # Находим блок новости "Сила в людях"
    # news_block = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='news-block']")))
    #
    # # Находим ссылку "Подробнее" в блоке новости "Сила в людях" и кликаем на нее
    # more_link = news_block.find_element(By.XPATH, ".//a[contains(text(), 'Подробнее')]")
    # more_link.click()

    # Проверяем, что открылась страница https://tensor.ru/about
# assert "https://tensor.ru/about" == driver.current_url
#
# # Закрываем браузер
finally:
    browser.quit()
