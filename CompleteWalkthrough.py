""" Test-case with following scenario: Add location -> add device to location -> add zone -> 
add SSID to zone -> add device to zone. """

import unittest
import logging

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# own
import address