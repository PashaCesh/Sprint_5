from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pages.authorization_page as ap
import pages.main_page as mp
import pages.account_page as acp
import config_files.config as c
from conftest import run_driver


class TestAccountPage:

    def test_account_page_by_clicking_on_account_main_page_button(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.sign_in_button).click()
        run_driver.find_element(By.XPATH, ap.email_input_field_authorization).send_keys(c.sign_in_email)
        run_driver.find_element(By.XPATH, ap.password_input_field_authorization).send_keys(c.sign_in_password)
        run_driver.find_element(By.XPATH, ap.sign_in_button_on_authorization_page).click()
        run_driver.find_element(By.XPATH, mp.account_button).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                              acp.profile_tab_account_page)))
        assert (acp.profile_tab_account_page_text in run_driver.find_element(By.XPATH, acp.profile_tab_account_page)
                .get_attribute("textContent"))

    def test_account_page_by_clicking_on_account_main_page_button_without_authorization(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.account_button).click()
        assert c.url_authorization in run_driver.current_url
