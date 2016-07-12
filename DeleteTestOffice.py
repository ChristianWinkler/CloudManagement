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

class deleteTestOffice(unittest.TestCase):
        
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
            self.driver.implicitly_wait(20)
            
        def test_delete_test_office(self):
            driver = self.driver
            driver.maximize_window()
            driver.get(self.base_url)
            driver.find_element_by_id("user_email").send_keys("vitalii.petruniak@sogeti.de")
            driver.find_element_by_id("user_password").send_keys("NatAw1988")
            driver.find_element_by_name("commit").click()
            """wait until home page will be loaded"""
            WebDriverWait(driver, 10).until(
                lambda element: element.find_element_by_xpath("//div[contains(.,'Locations')]").is_displayed(),
                'Timeout.')
            """click on locations"""
            driver.find_element_by_xpath("//md-content[@id='content']/section/md-content/div/home-dashboard/div/md-content/div/dashing/md-card/md-card-content/md-list-item[3]/div/a").click()
            WebDriverWait(driver, 10).until(
                lambda element: element.find_element_by_xpath("//div[contains(.,'Address')]").is_displayed(),
                'Timeout.')
            driver.find_element_by_link_text("Test office").click()
            WebDriverWait(driver, 10).until(
                lambda element: element.find_element_by_xpath("//div[contains(.,'Settings')]").is_displayed(),
                'Timeout.') 
            """click settings button"""
            driver.find_element_by_xpath("//md-content[@id='content']/section/md-sidenav[2]/md-content/ul/li[14]/menu-link/a/span").click()
            WebDriverWait(driver, 10).until(
                lambda element: element.find_element_by_xpath("//div[contains(.,'Details')]").is_displayed(),
                'Timeout.') 
            """deleting location""" 
            """clicking action button"""
            driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            """click delete"""
            driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
            """submit deleting"""
            driver.find_element_by_xpath("(//button[@type='button'])[34]").click()


        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
    

driver.close()