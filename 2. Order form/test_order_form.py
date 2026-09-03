import pytest_check as check

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_empty_required_fields_error_message(driver):
    driver.get("https://formdesigner.ru/examples/order.html")

    driver.find_element(By.ID, "c-p-bn").click()

    element = driver.find_element(By.ID, "form_1006")
    driver.execute_script("arguments[0].scrollIntoView();", element)

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".errorSummary")))

    errors = driver.find_elements(By.CSS_SELECTOR, ".errorSummary li")

    check.equal(errors[0].text, "Необходимо заполнить поле ФИО:.")
    check.equal(errors[1].text, "Необходимо заполнить поле E-mail.")
    check.equal(errors[2].text, "Необходимо заполнить поле Количество.")
    check.equal(errors[3].text, "Необходимо заполнить поле Дата доставки.")