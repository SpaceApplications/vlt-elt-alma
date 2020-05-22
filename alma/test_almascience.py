import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver(request):
    driver_name = request.config.getoption("--driver")

    driver_cls = {
        'firefox': webdriver.Firefox,
        'chrome': webdriver.Chrome,
        'edge': webdriver.Edge,
        'safari': webdriver.Safari,
    }[driver_name]

    driver = driver_cls()

    try:
        yield driver
    finally:
        driver.close()


def test_almascience(request, driver):
    ous_id = request.config.getoption("--ous_id")

    driver.get("https://almascience.eso.org/asax/")

    # Wait for page to be loaded
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'search-input-mous')))

    # Open the search menu
    search_button = driver.find_element_by_id('search-button')
    ActionChains(driver).move_to_element_with_offset(
        search_button, 1, 1).perform()

    # Type in the search parameter
    search_box.send_keys(ous_id)
    search_box.send_keys(Keys.RETURN)

    # Wait for the request to be fired
    time.sleep(5)

    # Check that we don't have an empty table
    assert len(driver.find_elements_by_class_name('empty-row')) == 0, \
        'The result set is empty'

    # Check that we have at least one observation
    scroller = driver.find_element_by_tag_name('datatable-scroller')
    assert len(scroller.find_elements_by_tag_name(
        'datatable-row-wrapper')) >= 1, \
        'There is no rows in the result set'
