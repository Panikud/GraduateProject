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

def test_auth_email_ELKW():
   # Открываем продукт ЕЛК Web
   pytest.driver.get(Auth_ELKW)
   # Переходим на страницу стандартной авторизации
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   # Переключаемся на вход через почту
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   # Вводим email
   pytest.driver.find_element(By.ID, 'username').send_keys(Email)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()
   # Нажимаем на иконку профиля, чтобы затем нажать на кнопку выхода
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_email_OnlaimW():
   # Открываем продукт Онлайм Web
   pytest.driver.get(Auth_OnlaimW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Email)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_email_StartW():
   # Открываем продукт Старт Web
   pytest.driver.get(Auth_StartW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Email)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_email_SmartHomeW():
   # Открываем продукт Умный дом Web
   pytest.driver.get(Auth_SmartHomeW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Email)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_email_KeyW():
   # Открываем продукт Ключ Web
   pytest.driver.get(Auth_KeyW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Email)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_phone_ELKW():
   pytest.driver.get(Auth_ELKW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Phone)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_phone_OnlaimW():
   pytest.driver.get(Auth_OnlaimW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Phone)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_phone_StartW():
   pytest.driver.get(Auth_StartW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Phone)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_phone_SmartHomeW():
   pytest.driver.get(Auth_SmartHomeW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Phone)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()

def test_auth_phone_KeyW():
   pytest.driver.get(Auth_KeyW)
   btn1 = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
   btn1.click()
   pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   pytest.driver.find_element(By.ID, 'username').send_keys(Phone)
   pytest.driver.find_element(By.ID, 'password').send_keys(Password)
   pytest.driver.find_element(By.ID, 'kc-login').click()
   pytest.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div[2]').click()
   pytest.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/button').click()