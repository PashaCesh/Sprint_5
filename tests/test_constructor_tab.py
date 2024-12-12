from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pages.main_page as mp
import config_files.config as c
from conftest import run_driver

class TestConstructorPage:

    def test_bun_tab_on_main_page(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.sauce_tab_on_main_page).click()
        run_driver.find_element(By.XPATH, mp.bun_tab_on_main_page).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                          mp.bun_header_on_main_page)))
        assert (mp.bun_header_on_main_page_text in run_driver.find_element(By.XPATH, mp.bun_header_on_main_page)
            .get_attribute("textContent"))

    def test_sauce_tab_on_main_page(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.sauce_tab_on_main_page).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                          mp.sauce_header_on_main_page)))
        assert (mp.sauce_header_on_main_page_text in run_driver.find_element(By.XPATH, mp.sauce_header_on_main_page)
            .get_attribute("textContent"))

    def test_fillings_tab_on_main_page(self, run_driver):
        run_driver.get(c.base_url)
        run_driver.find_element(By.XPATH, mp.fillings_tab_on_main_page).click()
        WebDriverWait(run_driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                          mp.fillings_header_on_main_page)))
        assert (mp.fillings_header_on_main_page_text in run_driver.find_element(By.XPATH, mp.fillings_header_on_main_page)
            .get_attribute("textContent"))