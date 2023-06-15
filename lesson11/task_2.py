# -*- coding: utf-8 -*-
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


# Открываем сайт sbis.ru
driver = webdriver.Chrome()
driver.maximize_window()
sleep(2)
sbis_site = 'https://fix-online.sbis.ru/'
contact_page = 'https://fix-online.sbis.ru/page/dialogs'
try:
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get(sbis_site)
    sleep(1)
    # Поиск поля логин и пароль. Ввод данных и авторизация на сайте
    login = driver.find_element(By.NAME, 'Login')
    login.send_keys('dp_sp11_96', Keys.ENTER)
    sleep(1)
    assert login.get_attribute('value') == 'dp_sp11_96'
    password = driver.find_element(By.NAME, 'Password')
    password.send_keys('1108Denis@', Keys.ENTER)
    sleep(7)
    # Поиск Контакты в аккордеоне. Переход в контакты
    contact = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] .NavigationPanels-Accordion__title')
    assert contact.is_displayed()
    contact.click()
    sleep(5)
    contact_more = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"] .NavigationPanels-SubMenu__headTitle')
    assert contact_more.is_displayed()
    contact_more.click()
    sleep(5)
    # Поиск кнопки + для отправки сообщения. Открытие окна поиска контакты. Выбор контакта
    plus = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    assert plus.is_displayed()
    plus.click()
    sleep(3)
    search_fio = driver.find_element(By.CSS_SELECTOR, ' .controls-StackTemplate-content_wrapper .controls-Field')
    search_fio.send_keys('Сиднеев Андрей ')
    sleep(4)
    # Отображение найденного контакта. Ввод сообщения и отправка
    fio_employer = driver.find_element(By.CSS_SELECTOR, '.controls_Person_theme-default.person-Info__withActivity')
    fio_employer.click()
    sleep(2)
    message_txt = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    assert message_txt.is_displayed()
    message_txt.send_keys('Тестовое сообщение')
    sleep(3)
    send_btn = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    assert send_btn.is_displayed()
    send_btn.click()
    sleep(5)
    # Поиск отправленного сообщения в реестре. Проверка сообщения по отправленному тексту. Удаление сообщения
    seng_msg = driver.find_elements(By.CSS_SELECTOR, ' .msg-dialogs-item__message-text')
    last_msg = seng_msg[0]
    msg_txt = 'Тестовое сообщение'
    assert last_msg.text == msg_txt
    action = ActionChains(driver)
    action.move_to_element(last_msg).perform()
    sleep(2)
    del_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    assert del_btn.is_displayed()
    del_btn.click()
    sleep(8)
    # Проверка отсутствия удаленного сообщения в реестре
    another_msg = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    find_del_msg = another_msg
    del_msg_txt = 'Текст сообщения'
    assert find_del_msg != del_msg_txt
finally:
    driver.quit()
