from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from elements.element import Element


class addLocation(Element):
    def execute(self, driver, config):
        driver.find_element_by_link_text("add_circle").click()
        WebDriverWait(driver, 20).until(
                                        EC.element_to_be_clickable((By.ID, "input_53"))
                                        )
        driver.find_element_by_id("input_53").clear()
        driver.find_element_by_id("input_53").send_keys(config["LocationData"]["new_name"])
        driver.find_element_by_id("input_54").clear()
        driver.find_element_by_id("input_54").send_keys(config["LocationData"]["new_address"])
        driver.find_element_by_id("input_55").clear()
        driver.find_element_by_id("input_55").send_keys(config["LocationData"]["new_city"])
        driver.find_element_by_id("input_56").clear()
        driver.find_element_by_id("input_56").send_keys(config["LocationData"]["new_postcode"])
        driver.find_element_by_xpath("//button[@type='submit']").submit()
        driver.find_element_by_class_name("devolo_logo_lg").click()
        print "The test is done"