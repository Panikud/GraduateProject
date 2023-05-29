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

def test_timedcode_fields_ELKW():
    pytest.driver.get(Auth_ELKW)
    pytest.driver.implicitly_wait(3)

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/span[2]')
    assert enter.text == 'E-mail или мобильный телефон'
    code_btn = pytest.driver.find_element(By.ID, 'otp_get_code')
    assert code_btn.text == 'Получить код'
    standard_btn = pytest.driver.find_element(By.ID, 'standard_auth_btn')
    assert standard_btn.text == 'Войти с паролем'

def test_timedcode_fields_OnlimeW():
    pytest.driver.get(Auth_OnlaimW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'back_to_otp_btn')))
    btn1.click()

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/span[2]')
    assert enter.text == 'E-mail или мобильный телефон'
    code_btn = pytest.driver.find_element(By.ID, 'otp_get_code')
    assert code_btn.text == 'Получить код'
    standard_btn = pytest.driver.find_element(By.ID, 'standard_auth_btn')
    assert standard_btn.text == 'Войти с паролем'

def test_timedcode_fields_StartW():
    pytest.driver.get(Auth_StartW)
    pytest.driver.implicitly_wait(3)

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/span[2]')
    assert enter.text == 'E-mail или мобильный телефон'
    code_btn = pytest.driver.find_element(By.ID, 'otp_get_code')
    assert code_btn.text == 'Получить код'
    standard_btn = pytest.driver.find_element(By.ID, 'standard_auth_btn')
    assert standard_btn.text == 'Войти с паролем'

def test_timedcode_fields_SmartHomeW():
    pytest.driver.get(Auth_SmartHomeW)
    pytest.driver.implicitly_wait(3)

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/span[2]')
    assert enter.text == 'E-mail или мобильный телефон'
    code_btn = pytest.driver.find_element(By.ID, 'otp_get_code')
    assert code_btn.text == 'Получить код'
    standard_btn = pytest.driver.find_element(By.ID, 'standard_auth_btn')
    assert standard_btn.text == 'Войти с паролем'

def test_timedcode_fields_KeyW():
    pytest.driver.get(Auth_KeyW)
    btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div[2]/a[1]')))
    btn1.click()

    enter = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/span[2]')
    assert enter.text == 'E-mail или мобильный телефон'
    code_btn = pytest.driver.find_element(By.ID, 'otp_get_code')
    assert code_btn.text == 'Получить код'
    standard_btn = pytest.driver.find_element(By.ID, 'standard_auth_btn')
    assert standard_btn.text == 'Войти с паролем'