from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators


def test_sign_up_positive(generate_email, generate_pass, driver):
    driver.get(locators.signup_url)

    driver.find_element(By.XPATH, locators.signup_name_xpath).send_keys(generate_email)
    driver.find_element(By.XPATH, locators.signup_email_xpath).send_keys(generate_email)
    driver.find_element(By.XPATH, locators.signup_pass_xpath).send_keys(generate_pass)
    driver.find_element(By.XPATH, locators.signup_signup_button_class).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_forgot_pass_xpath)))

    #запускаем функцию еще раз если такой пользователь существует
    errors = driver.find_elements(By.CLASS_NAME, locators.signup_user_exist_error_class)
    if errors:
        driver.quit()
        test_sign_up_positive()
    else:
        assert driver.current_url == locators.login_url


def test_sign_up_incorrect_pass_error(driver):
    driver.get(locators.signup_url)

    driver.find_element(By.XPATH, locators.signup_pass_xpath).send_keys('123')
    driver.find_element(By.XPATH, locators.signup_email_xpath).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.signup_pass_error_xpath)))
    errors = driver.find_elements(By.XPATH, locators.signup_pass_error_xpath)

    assert len(errors) == 1

