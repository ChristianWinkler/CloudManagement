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
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# own
import address


class addLocations(unittest.TestCase):

    def setUp(self):
        
        #use local browser
        self.driver = webdriver.Firefox()
        
        # use selenium grid
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

    def test_add_location(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_id("user_email").send_keys("vitalii.petruniak@sogeti.de")
        driver.find_element_by_id("user_password").send_keys("NatAw1988")
        driver.find_element_by_name("commit").click()
        #wait until home page will be loaded
        WebDriverWait(driver, 30).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Locations')]").is_displayed(),
            'Timeout my friend.'
                                        )
        #click to add location
        driver.find_element_by_xpath("//md-content[@id='content']/section/md-content/div/home-dashboard/div/section/md-toolbar/div/a/md-icon").click()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Please enter a location name')]").is_displayed(),
            'Timeout.')
        #generating location names
        NewName = address.generateName(5, 30)
        NewAddress = address.generateAddress(6, 50)
        NewCity = address.generateCity(3, 20)
        NewPostcode = address.generatePostcode(2, 8)
        print NewName
        driver.find_element_by_id("input_53").clear()
        driver.find_element_by_id("input_53").send_keys(NewName)
        driver.find_element_by_id("input_54").clear()
        driver.find_element_by_id("input_54").send_keys(NewAddress)
        driver.find_element_by_id("input_55").clear()
        driver.find_element_by_id("input_55").send_keys(NewCity)
        driver.find_element_by_id("input_56").clear()
        driver.find_element_by_id("input_56").send_keys(NewPostcode)
        SaveButton = driver.find_element_by_xpath("//button[@type='submit']").submit()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Please Add a Device')]").is_displayed(),
            'Timeout.')
        #go to the home page
        driver.find_element_by_css_selector("img.devolo_logo.devolo_logo_lg").submit()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Locations')]").is_displayed(),
            'Timeout.')
        driver.find_element_by_xpath("//md-content[@id='content']/section/md-content/div/home-dashboard/div/md-content/div/dashing/md-card/md-card-content/md-list-item[3]/div/a").click()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Address')]").is_displayed(),
            'Timeout.')
        driver.find_element_by_link_text(NewName).click()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Settings')]").is_displayed(),
            'Timeout.') 
        #click settings button
        driver.find_element_by_xpath("//md-content[@id='content']/section/md-sidenav[2]/md-content/ul/li[14]/menu-link/a/span").click()
        WebDriverWait(driver, 10).until(
            lambda element: element.find_element_by_xpath("//div[contains(.,'Details')]").is_displayed(),
            'Timeout.') 
        # deleting location 
        # clicking action button
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        # click delete
        driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
        # submit deleting 
        driver.find_element_by_xpath("(//button[@type='button'])[34]").click()
        
    
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
    

driver.close()
