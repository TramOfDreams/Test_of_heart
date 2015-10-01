#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MouseOnHeart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_click_on_heart(self):
         self.driver.get('http://fillo.fshome/share/test.html')
         WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.text')))
         
         heart = self.driver.find_element_by_css_selector('.heart')
         ActionChains(self.driver).move_to_element(heart).drag_and_drop(heart,heart).perform()
         WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.text')))
         
         ActionChains(self.driver).move_by_offset(200,180).perform()
         WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.text')))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()