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
        for i in range(1, rowCount+1):
                object = driver.find_element_by_xpath("//table/tbody/tr["+str(i)+"]/td[2]/a").text
                n = object
                LocationList.append(n)
        print LocationList
        
        # click on the second location
        driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]/a").click()
        #wait till settings will be clickable
        element = WebDriverWait(driver, 20).until(
                                                      EC.element_to_be_clickable((By.XPATH, '//md-sidenav[2]/md-content/ul/li[14]/menu-link/a/span'))
                                                      )
        element.click()
        # deleting location
        driver.find_element_by_xpath("//location-settings-menu/md-menu/button").click()
        element = WebDriverWait(driver, 20).until(
                                                      EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[6]"))
                                                      )
        element.click()
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[34]").click()
        
        