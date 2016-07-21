from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from elements.element import Element

LocationList = []
rowCount = 0
n = 0

class doLocationList (Element):

    def execute(self, driver, config):
        #clicking on "Locations"
        driver.find_element_by_xpath("//md-card-content/md-list-item[3]/div/a").click()
        #wait until all locations be there
        element = WebDriverWait(driver, 20).until(
                                              EC.element_to_be_clickable((By.XPATH, '//table'))
                                              )
        
        #create a list of locations
        
        
        rowCount = len(driver.find_elements(By.XPATH, "//table/tbody/tr"))
        elements = driver.find_elements(By.XPATH, "//table/tbody/tr/td")
        print elements.text
        """for i in range(rowCount):
            if n < rowCount[i]:
                element = driver.find_element_by_xpath("//table/tbody/tr/td/a").text
                print element
                n = element
                i = ++i
                LocationList.append(n)
        print LocationList"""
        