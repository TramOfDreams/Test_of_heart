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
         heart = self.driver.find_element_by_css_selector('.heart')
         ActionChains(self.driver).move_to_element(heart).drag_and_drop(heart,heart).perform()
         WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.text')))
         #div = self.driver.find_element_by_css_selector('.text[div*=!]')
         #print(div)
         #param = u'Аум!'
         not_heart = self.driver.find_element_by_css_selector(':not(.heart)')
         ActionChains(self.driver).move_to_element(not_heart).click_and_hold().perform()
         self.assertTrue(self.driver.find_element_by_css_selector('.heart:not(hover)'))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()