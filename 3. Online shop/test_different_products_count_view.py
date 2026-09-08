from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_different_products_count_view(driver):
    driver.get("https://demowebshop.tricentis.com/books")

    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.presence_of_element_located((By.ID, "products-pagesize")))

    items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    assert len(items) <= 8

    select_element = driver.find_element(By.ID, "products-pagesize")
    Select(select_element).select_by_visible_text("4")

    wait.until(expected_conditions.staleness_of(select_element))

    items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    assert len(items) <= 4