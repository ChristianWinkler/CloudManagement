# -*- coding: utf-8 -*-

import site

import unittest
import logging

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# own
import address


class addDevice(unittest.TestCase):

    def setUp(self):
        
        """use local browser"""
        self.driver = webdriver.Firefox()
        
        """use selenium grid"""
        #self.driver = webdriver.Remote(
        #                               command_executor='http://selenium-hub.dvt.intern:80/wd/hub',
        #                               desired_capabilities={
        #                                    "browserName": "firefox",
        #                                    "version": "ESR",
        #                                    "platform": "MAC",
        #                                    "javascriptEnabled": "True"
        #                                                     }
        #                               )
        self.base_url = "https://bs-ct-dev.devolo.net/#/"
        self.driver.implicitly_wait(30)
        
    def test_add_device(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_id("user_email").send_keys("vitalii.petruniak@sogeti.de")
        driver.find_element_by_id("user_password").send_keys("NatAw1988")
        driver.find_element_by_name("commit").click()
        WebDriverWait(driver, 30).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'locations')]").is_displayed(),
            'Timeout.')
        driver.find_element_by_xpath("//md-content[@id='content']/section/md-content/div/home-dashboard/div/section/md-toolbar/div/a/md-icon").click()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Please enter a location name')]").is_displayed(),
            'Timeout.')
        driver.find_element_by_id("input_53").clear()
        driver.find_element_by_id("input_53").send_keys("Test office")
        driver.find_element_by_id("input_54").clear()
        driver.find_element_by_id("input_54").send_keys("Test address")
        driver.find_element_by_id("input_55").clear()
        driver.find_element_by_id("input_55").send_keys("Test city")
        driver.find_element_by_id("input_56").clear()
        driver.find_element_by_id("input_56").send_keys("12345678")
        SaveButton = driver.find_element_by_xpath("//button[@type='submit']").submit()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Please Add a Device')]").is_displayed(),
            'Timeout my friend.')
        """adding new device"""
        driver.find_element_by_css_selector("md-card-actions.layout-align-end-center.layout-row > button.md-button.md-ink-ripple").click()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//md-radio-button[@aria-label='Enter MAC Address']").submit(),
            'Timeout my friend.')
        driver.find_element_by_id("input_2746").send_keys("30-D3-2D-45-70-EA")
        driver.find_element_by_id("input_2747").send_keys("1200i_VP")
        driver.find_element_by_xpath("//button[@type='submit']").click()  
        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
    

driver.close()
  
        
    