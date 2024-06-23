import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


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

    driver.find_element(By.XPATH, locators.login_email_xpath).send_keys(data.email)
    driver.find_element(By.XPATH, locators.login_pass_xpath).send_keys(data.password)
    driver.find_element(By.XPATH, locators.login_login_button_xpath).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.main_page_checkout_xpath)))
