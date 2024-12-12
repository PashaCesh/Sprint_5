from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pages.registration_page as rp
import pages.authorization_page as ap
import config_files.config as c
from conftest import run_driver

class TestRegistrationPage:

    def test_register_on_the_website(self, run_driver):
        run_driver.get(c.url_registration)
        run_driver.find_element(By.XPATH, rp.name_input_field).send_keys(c.username)
        run_driver.find_element(By.XPATH, rp.email_input_field).send_keys(c.sign_up_email)
        run_driver.find_element(By.XPATH, rp.password_input_field).send_keys(c.sign_up_password)
        run_driver.find_element(By.XPATH, rp.registration_button).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                              ap.authorization_header)))
        assert c.url_authorization in run_driver.current_url


    def test_register_with_incorrect_password(self, run_driver):
        run_driver.get(c.url_registration)
        run_driver.find_element(By.XPATH, rp.password_input_field).send_keys(c.incorrect_password)
        run_driver.find_element(By.XPATH, rp.email_input_field).click()
        assert (rp.error_text_in_password_field in run_driver.find_element(By.XPATH, rp.error_in_password_field)
            .get_attribute("textContent"))
