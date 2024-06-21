import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import locators


@pytest.mark.parametrize('ingredient', ['Булки', 'Соусы', 'Начинки'])
def test_constructor_scroll(driver, ingredient):
    driver.get(locators.main_page_url)
    if ingredient == 'Булки': #отматываем вниз чтобы первая кнопка стала доступной
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//img[@alt='Сыр с астероидной плесенью']"))

    driver.find_element(By.XPATH, f"//span[text()='{ingredient}']").click()
    assert expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, By.XPATH, f"//span[text()='{ingredient}']/parent::div"), 'text()', 'tab_tab_type_current')
