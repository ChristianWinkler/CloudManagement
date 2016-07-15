from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from elements.element import Element

class deleteLocations(Element):
    def execute(self, driver, config):
        driver.find_element_by_xpath("//md-content[@id='content']/section/md-content/div/home-dashboard/div/md-content/div/dashing/md-card/md-card-content/md-list-item[3]/div/a").click() #click on locations
        WebDriverWait(driver, 20).until(
            lambda element: element.find_element_by_class_name("intercom-launcher-button").is_displayed(),
            'Timeout.')
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click() #open action menu
        driver.find_element_by_xpath("//div[@id='menu_container_54']/md-menu-content/md-menu-item/a").click() #open view location
        driver.find_element_by_xpath("//md-content[@id='content']/section/md-sidenav[2]/md-content/ul/li[14]/menu-link/a").click() # open settings
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click() # open action menu 
        driver.find_element_by_xpath("(//button[@type='button'])[31]").click() # click delete 
        driver.find_element_by_xpath("(//button[@type='button'])[33]").click() # submit delete
        #findElements(By.xpath("//*[contains(text(),'" + text + "')]"))