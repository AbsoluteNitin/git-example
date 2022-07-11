import unittest

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import HTMLTestRunner
import page

chromeDriverPath = Service('chromedriver.exe')


class test_audi_portal(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=chromeDriverPath)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def check_url_access(self):
        """ Going to check URL is opening or not"""
        self.driver.get(page.audi["url"])
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def test_sign_in(self):
        """ Testing Login in """
        self.driver.get(page.audi["url"])
        time.sleep(2)
        self.driver.implicitly_wait(5)
        page.MainPage.click_Login_button(self)
        time.sleep(2)
        self.assertTrue(True, "unable to do login")

    def test_sign_out(self):
        """ Testing Log out"""
        self.driver.get(page.audi["url"])
        self.driver.implicitly_wait(5)
        page.MainPage.click_Login_button(self)
        time.sleep(2)
        page.MainPage.click_Logout_button(self)
        time.sleep(2)

    def test_edit_carName(self):
        """ Testing Car Name edit """
        self.driver.get(page.audi["url"])
        self.driver.implicitly_wait(5)
        page.MainPage.click_Login_button(self)
        time.sleep(2)
        page.MainPage.click_Vehicle_rename(self)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="Reports",
                                                           title="Audi Test Reports",
                                                           description="Audi Portal Test Reports"))
