from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pages.authorization_page as ap
import pages.main_page as mp
import config_files.config as c
from conftest import run_driver

class TestHeaderTab:

    def test_header_tab_by_clicking_on_constructor_main_page_button(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.sign_in_button).click()
        run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
        run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
        run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
        run_driver.find_element(By.XPATH, mp.account_button).click()
        run_driver.find_element(By.XPATH, mp.constructor_button).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH, mp.title_on_main_page)))
        assert (mp.title_on_main_page_text in run_driver.find_element(By.XPATH, mp.title_on_main_page)
            .get_attribute("textContent"))

    def test_header_tab_by_clicking_on_stellar_burger_main_page_button(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.sign_in_button).click()
        run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
        run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
        run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
        run_driver.find_element(By.XPATH, mp.account_button).click()
        run_driver.find_element(By.XPATH, mp.constructor_button).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH, mp.title_on_main_page)))
        assert (mp.title_on_main_page_text in run_driver.find_element(By.XPATH, mp.title_on_main_page)
            .get_attribute("textContent"))