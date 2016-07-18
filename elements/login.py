from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from elements.element import Element

class Login(Element):
    def execute(self, driver, config):
        login_password = driver.find_element_by_id("user_email")
        login_password.send_keys(config["Login"]["login"])
        login_password = driver.find_element_by_id("user_password")
        login_password.send_keys(config["Login"]["password"])
        login_password.send_keys(Keys.RETURN)
        WebDriverWait(driver, 20).until(
                                        EC.element_to_be_clickable((By.XPATH, "//md-content[@id='content']/section/md-content/div/home-dashboard/div/md-content/div/dashing/md-card/md-card-content/md-list-item[3]/div/a"))
                                        )