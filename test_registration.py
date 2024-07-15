import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome() #installed chromedriver and then added in path in system properties
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    driver.quit()


def test_valid_input_data(driver):
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1990")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("January")
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--001").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
    driver.find_element(By.ID, "currentAddress").send_keys("123 Main St")
    driver.find_element(By.ID, "submit").click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert "Thanks for submitting the form" in confirmation_message.text


def test_successful_password_match(driver):
    driver.find_element(By.ID, "firstName").send_keys("Jane")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("jane.doe@example.com")
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1992")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("February")
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--002").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Physics")
    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
    driver.find_element(By.ID, "currentAddress").send_keys("456 Elm St")
    driver.find_element(By.ID, "submit").click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert "Thanks for submitting the form" in confirmation_message.text


def test_invalid_email_format(driver):
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john.doe@com")
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1990")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("January")
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--001").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
    driver.find_element(By.ID, "currentAddress").send_keys("123 Main St")
    driver.find_element(By.ID, "submit").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".was-validated .form-control:invalid"))
    )
    assert "email" in error_message.get_attribute("validationMessage").lower()


def test_password_mismatch(driver):
    driver.find_element(By.ID, "firstName").send_keys("Jane")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("jane.doe@example.com")
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1992")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("February")
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--002").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Physics")
    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
    driver.find_element(By.ID, "currentAddress").send_keys("456 Elm St")
    driver.find_element(By.ID, "submit").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".was-validated .form-control:invalid"))
    )
    assert "match" in error_message.get_attribute("validationMessage").lower()
