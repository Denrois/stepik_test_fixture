from selenium.webdriver.common.by import By


def test_presence_add_to_basket_el(driver):
    driver.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_basket = driver.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').is_enabled()
    assert add_to_basket is True


