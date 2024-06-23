from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import locators


class TestMainScroll:

    def test_constructor_scroll_buns_positive(self, driver):
        driver.get(locators.main_page_url)
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, locators.main_last_scroll_item))
        driver.find_element(By.XPATH, locators.main_scroll_buns_xpath).click()
        assert expected_conditions.text_to_be_present_in_element_attribute(
            (By.XPATH, locators.main_scroll_buns_parent_xpath), 'text()', 'tab_tab_type_current')

    def test_constructor_scroll_sauce_positive(self, driver):
        driver.get(locators.main_page_url)

        driver.find_element(By.XPATH, locators.main_scroll_sauces_xpath).click()
        assert expected_conditions.text_to_be_present_in_element_attribute(
            (By.XPATH, locators.main_scroll_sauces_parent_xpath),
            'text()', 'tab_tab_type_current')

    def test_constructor_scroll_filling_positive(self, driver):
        driver.get(locators.main_page_url)

        driver.find_element(By.XPATH, locators.main_scroll_fillings_xpath).click()
        assert expected_conditions.text_to_be_present_in_element_attribute(
            (By.XPATH, locators.main_scroll_fillings_parent_xpath),
            'text()', 'tab_tab_type_current')
