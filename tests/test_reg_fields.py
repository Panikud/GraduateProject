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

def test_reg_fields_ELKW():
    pytest.driver.get(Auth_ELKW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn1.click()
    btn2 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    btn2.click()

    firstname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    assert firstname.text == 'Имя'
    lastname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert lastname.text == 'Фамилия'

    region = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')
    assert region.text == 'Регион'
    mailphone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/div/span[2]')
    assert mailphone.text == 'E-mail или мобильный телефон'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    assert password.text == 'Пароль'
    password2 = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')
    assert password2.text == 'Подтверждение пароля'

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    assert enter.text == 'Продолжить'

def test_reg_fields_StartW():
    pytest.driver.get(Auth_StartW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn1.click()
    btn2 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    btn2.click()

    firstname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    assert firstname.text == 'Имя'
    lastname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert lastname.text == 'Фамилия'

    region = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')
    assert region.text == 'Регион'
    mailphone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/div/span[2]')
    assert mailphone.text == 'E-mail или мобильный телефон'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    assert password.text == 'Пароль'
    password2 = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')
    assert password2.text == 'Подтверждение пароля'

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    assert enter.text == 'Продолжить'

def test_reg_fields_SmartHomeW():
    pytest.driver.get(Auth_SmartHomeW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn1.click()
    btn2 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    btn2.click()

    firstname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    assert firstname.text == 'Имя'
    lastname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert lastname.text == 'Фамилия'

    region = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')
    assert region.text == 'Регион'
    mailphone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/div/span[2]')
    assert mailphone.text == 'E-mail или мобильный телефон'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    assert password.text == 'Пароль'
    password2 = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')
    assert password2.text == 'Подтверждение пароля'

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    assert enter.text == 'Продолжить'

def test_reg_fields_KeyW():
    pytest.driver.get(Auth_KeyW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div[2]/a[1]')))
    btn1.click()
    btn2 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    btn2.click()
    btn3 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    btn3.click()

    firstname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    assert firstname.text == 'Имя'
    lastname = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    assert lastname.text == 'Фамилия'

    region = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')
    assert region.text == 'Регион'
    mailphone = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/div/span[2]')
    assert mailphone.text == 'E-mail или мобильный телефон'

    password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    assert password.text == 'Пароль'
    password2 = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')
    assert password2.text == 'Подтверждение пароля'

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    assert enter.text == 'Продолжить'