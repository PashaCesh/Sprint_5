import pytest

from selenium import webdriver

@pytest.fixture
def run_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()