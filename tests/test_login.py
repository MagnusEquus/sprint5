import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators

# разбил тесты на отдельную проверку логина и переходы на эту страницу с разных страниц сайта
def test_login_positive(driver):
    driver.get(locators.login_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_login_button_xpath)))
    driver.find_element(By.XPATH, locators.login_email_xpath).send_keys('123+123@yandex.ru')
    driver.find_element(By.XPATH, locators.login_pass_xpath).send_keys('123+123@yandex.ru')
    driver.find_element(By.XPATH, locators.login_login_button_xpath).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.main_page_checkout_xpath)))

    assert locators.main_page_url in driver.current_url


@pytest.mark.parametrize('start_page, login_button', [
    [locators.main_page_url, locators.main_page_login_xpath],
    [locators.main_page_url, locators.main_page_account_login_xpath],
    [locators.signup_url, locators.signup_login_xpath],
    [locators.forgot_pass_url, locators.forgot_pass_login_link_xpath]
])
def test_main_to_login_page(start_page, login_button, driver):
    driver.get(start_page)
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_login_button_xpath)))
    assert locators.login_url in driver.current_url
