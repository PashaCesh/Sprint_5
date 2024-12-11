from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pages.authorization_page as ap
import pages.main_page as mp
import pages.registration_page as rp
import pages.password_recovery_page as prp
import config_files.config as c
from conftest import run_driver


set_an_order_button_text = 'Оформить заказ'

def test_authorization_by_clicking_on_main_page_sign_in_button(run_driver):
    run_driver.get(c.base_url)
    run_driver.find_element(By.XPATH, mp.sign_in_button).click()
    run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
    run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
    run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
    WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH, mp.set_an_order_button)))
    assert (set_an_order_button_text in run_driver.find_element(By.XPATH, mp.set_an_order_button)
            .get_attribute("textContent"))

def test_authorization_by_clicking_on_main_page_account_button(run_driver):
    run_driver.get(c.base_url)
    run_driver.find_element(By.XPATH, mp.account_button).click()
    run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
    run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
    run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
    WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH, mp.set_an_order_button)))
    assert (set_an_order_button_text in run_driver.find_element(By.XPATH, mp.set_an_order_button)
            .get_attribute("textContent"))

def test_authorization_by_clicking_on_registration_page_sign_in_button(run_driver):
    run_driver.get(c.url_registration)
    run_driver.find_element(By.XPATH, rp.registration_sign_in_button).click()
    run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
    run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
    run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
    WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH, mp.set_an_order_button)))
    assert (set_an_order_button_text in run_driver.find_element(By.XPATH, mp.set_an_order_button)
            .get_attribute("textContent"))

def test_authorization_by_clicking_on_password_recovery_page_sign_in_button(run_driver):
    run_driver.get(c.url_password_recovery)
    run_driver.find_element(By.XPATH, prp.password_recovery_sign_in_button).click()
    run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
    run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
    run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
    WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH, mp.set_an_order_button)))
    assert (set_an_order_button_text in run_driver.find_element(By.XPATH, mp.set_an_order_button)
            .get_attribute("textContent"))