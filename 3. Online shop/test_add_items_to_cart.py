import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.mark.parametrize("query", ["Laptop", "Smartphone", "Fiction"])
def test_add_items_to_cart(driver, query):
    driver.get("https://demowebshop.tricentis.com/")

    driver.find_element(By.ID, "small-searchterms").send_keys(query)

    search_button = driver.find_element(By.CSS_SELECTOR, "input.search-box-button")
    search_button.click()

    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.staleness_of(search_button))

    first_item = driver.find_elements(By.CSS_SELECTOR, ".product-item")[0]
    product_name = first_item.find_element(By.CSS_SELECTOR, "h2.product-title a").text
    first_item.find_element(By.CSS_SELECTOR, "input[value='Add to cart']").click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, "#bar-notification.success")
    ))

    driver.find_element(By.CLASS_NAME, "cart-label").click()

    wait.until(expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, "td.product")
    ))

    cart_names = [e.text for e in driver.find_elements(By.CSS_SELECTOR, "td.product a.product-name")]
    assert product_name in cart_names