from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config import *

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(executable_path=Path)
   yield
   pytest.driver.quit()

def test_auth_fields_ELKW():
    pytest.driver.get(Auth_ELKW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn1.click()

    # Сохраняем элемент в переменную, чтобы проверить наличие поля и его название
    method_phone = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    assert method_phone.text == 'Телефон'
    method_phone.click()
    phone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert phone.text == 'Мобильный телефон'

    method_email = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    assert method_email.text == 'Почта'
    method_email.click()
    email = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert email.text == 'Электронная почта'

    method_login = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    assert method_login.text == 'Логин'
    method_login.click()
    login = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert login.text == 'Логин'

    method_ls = pytest.driver.find_element(By.ID, 't-btn-tab-ls')
    assert method_ls.text == 'Лицевой счёт'
    method_ls.click()
    ls = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert ls.text == 'Лицевой счёт'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    assert password.text == 'Пароль'
    enter = pytest.driver.find_element(By.ID, 'kc-login')
    assert enter.text == 'Войти'

def test_auth_fields_OnlaimW():
    pytest.driver.get(Auth_OnlaimW)
    pytest.driver.implicitly_wait(10)

    # Сохраняем элемент в переменную, чтобы проверить наличие поля и его название
    method_phone = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    assert method_phone.text == 'Телефон'
    method_phone.click()
    phone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert phone.text == 'Мобильный телефон'

    method_email = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    assert method_email.text == 'Почта'
    method_email.click()
    email = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert email.text == 'Электронная почта'

    method_login = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    assert method_login.text == 'Логин'
    method_login.click()
    login = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert login.text == 'Логин'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    assert password.text == 'Пароль'
    enter = pytest.driver.find_element(By.ID, 'kc-login')
    assert enter.text == 'Войти'

def test_auth_fields_StartW():
    pytest.driver.get(Auth_StartW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn1.click()

    # Сохраняем элемент в переменную, чтобы проверить наличие поля и его название
    method_phone = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    assert method_phone.text == 'Телефон'
    method_phone.click()
    phone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert phone.text == 'Мобильный телефон'

    method_email = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    assert method_email.text == 'Почта'
    method_email.click()
    email = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert email.text == 'Электронная почта'

    method_login = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    assert method_login.text == 'Логин'
    method_login.click()
    login = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert login.text == 'Логин'

    method_ls = pytest.driver.find_element(By.ID, 't-btn-tab-ls')
    assert method_ls.text == 'Лицевой счёт'
    method_ls.click()
    ls = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert ls.text == 'Лицевой счёт'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    assert password.text == 'Пароль'
    enter = pytest.driver.find_element(By.ID, 'kc-login')
    assert enter.text == 'Войти'

def test_auth_fields_SmartHomeW():
    pytest.driver.get(Auth_SmartHomeW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn1.click()

    # Сохраняем элемент в переменную, чтобы проверить наличие поля и его название
    method_phone = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    assert method_phone.text == 'Телефон'
    method_phone.click()
    phone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert phone.text == 'Мобильный телефон'

    method_email = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    assert method_email.text == 'Почта'
    method_email.click()
    email = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert email.text == 'Электронная почта'

    method_login = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    assert method_login.text == 'Логин'
    method_login.click()
    login = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert login.text == 'Логин'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    assert password.text == 'Пароль'
    enter = pytest.driver.find_element(By.ID, 'kc-login')
    assert enter.text == 'Войти'

def test_auth_fields_KeyW():
    pytest.driver.get(Auth_KeyW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div[2]/a[1]')))
    btn1.click()
    btn2 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn2.click()

    # Сохраняем элемент в переменную, чтобы проверить наличие поля и его название
    method_phone = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    assert method_phone.text == 'Телефон'
    method_phone.click()
    phone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert phone.text == 'Мобильный телефон'

    method_email = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    assert method_email.text == 'Почта'
    method_email.click()
    email = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert email.text == 'Электронная почта'

    method_login = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    assert method_login.text == 'Логин'
    method_login.click()
    login = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert login.text == 'Логин'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    assert password.text == 'Пароль'
    enter = pytest.driver.find_element(By.ID, 'kc-login')
    assert enter.text == 'Войти'