import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


@pytest.fixture
def generate_email():
    number = random.randint(100,99999)
    email = f'123+{number}@yandex.ru'
    return email

@pytest.fixture
def generate_pass():
    password = random.randint(100000, 999999999)
    return password

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.get(locators.login_url)
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_login_button_xpath)))

    driver.find_element(By.XPATH, locators.login_email_xpath).send_keys('123+123@yandex.ru')
    driver.find_element(By.XPATH, locators.login_pass_xpath).send_keys('123+123@yandex.ru')
    driver.find_element(By.XPATH, locators.login_login_button_xpath).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.main_page_checkout_xpath)))
