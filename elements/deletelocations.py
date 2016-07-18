from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from elements.element import Element

class deleteLocations(Element):
    def execute(self, driver, config):
        driver.find_element_by_xpath()