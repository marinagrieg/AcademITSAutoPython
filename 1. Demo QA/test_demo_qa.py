import os
import pytest_check as check

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

def test_practice_form(driver):
    wait = WebDriverWait(driver, 3)

    driver.get("https://demoqa.com/automation-practice-form")

    wait.until(expected_conditions.visibility_of_element_located((By.ID, "firstName")))
    driver.find_element(By.ID, "firstName").send_keys("Тест")
    driver.find_element(By.ID, "lastName").send_keys("Тестов")

    driver.find_element(By.ID, "userEmail").send_keys("test@test.com")
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()
    Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_visible_text("1994")
    Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_visible_text("December")
    driver.find_element(By.XPATH, "//div[@aria-label='Choose Thursday, December 15th, 1994']").click()

    driver.find_element(By.TAG_NAME, "body").click()

    driver.find_element(By.ID, "subjectsInput").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("C")

    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "subjects-auto-complete__option")))
    options = driver.find_elements(By.CLASS_NAME, "subjects-auto-complete__option")

    for option in options:
        if option.text == "Computer Science":
            option.click()

            break

    driver.find_element(By.ID, "hobbies-checkbox-3").click()

    photo_path = os.path.abspath("1. Demo QA/IMG_1855.JPG")
    driver.find_element(By.ID, "uploadPicture").send_keys(photo_path)

    driver.find_element(By.ID, "currentAddress").send_keys("ул. Тестовая, д. 0, кв. 0")

    driver.find_element(By.ID, "state").click()
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "react-select-3-listbox")))
    options = driver.find_elements(By.CSS_SELECTOR, "#react-select-3-listbox [role='option']")

    for option in options:
        if option.text == "NCR":
            option.click()

            break

    driver.find_element(By.ID, "city").click()
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "react-select-4-listbox")))
    options = driver.find_elements(By.CSS_SELECTOR, "#react-select-4-listbox [role='option']")

    for option in options:
        if option.text == "Delhi":
            option.click()

            break

    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit)

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, "example-modal-sizes-title-lg")
    ))

    rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
    result = {}

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        result[cells[0].text] = cells[1].text

    check.equal(result["Student Name"], "Тест Тестов")
    check.equal(result["Student Email"], "test@test.com")
    check.equal(result["Gender"], "Male")
    check.equal(result["Mobile"], "0123456789")
    check.equal(result["Date of Birth"], "15 December,1994")
    check.equal(result["Subjects"], "Computer Science")
    check.equal(result["Hobbies"], "Music")
    check.equal(result["Picture"], "IMG_1855.JPG")
    check.equal(result["Address"], "ул. Тестовая, д. 0, кв. 0")
    check.equal(result["State and City"], "NCR Delhi")