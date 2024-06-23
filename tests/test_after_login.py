import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators


class TestAfterLogin:

    def test_goto_account_page(self, driver, login):
        driver.find_element(By.XPATH, locators.main_page_account_login_xpath).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_save_button_xpath)))
        assert locators.profile_page_url in driver.current_url

    @pytest.mark.parametrize('test_element', [locators.profile_logo_xpath, locators.profile_main_page_button_xpath])
    def test_goto_main_page(self, test_element, driver, login):
        driver.find_element(By.XPATH, locators.main_page_account_login_xpath).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_save_button_xpath)))
        driver.find_element(By.XPATH, test_element).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.main_page_checkout_xpath)))
        assert driver.current_url == locators.main_page_url

    def test_logout_positive(self, driver, login):
        driver.find_element(By.XPATH, locators.main_page_account_login_xpath).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_save_button_xpath)))
        driver.find_element(By.XPATH, locators.profile_logout_button_xpath).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_login_button_xpath)))
        assert driver.current_url == locators.login_url
