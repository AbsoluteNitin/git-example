from element import BasePageElement
from locators import MainPageLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

audi = {
    "url": "https://ivehicle.myaudiconnect.nscindia.co.in/",
    "username": "audiprod123@gmail.com",
    "password": "Test@1234"
}


def elementClick(self, locator, locatorType="id"):
    try:
        element = self.getElement(locator, locatorType)
        element.click()
        self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        return True
    except Exception as er:
        self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
        return False

def sendKeys_wrapper(self,locator,):
    pass

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_Login_button(self):
        self.driver.find_element(*MainPageLocators.User_name).send_keys(audi["username"])
        self.driver.find_element(*MainPageLocators.Password_value).send_keys(audi["password"])
        element = self.driver.find_element(*MainPageLocators.Login_BUTTON)
        element.click()

    def click_Logout_button(self):
        element = self.driver.find_element(*MainPageLocators.Signout_option)
        element.click()
        element = self.driver.find_element(*MainPageLocators.Signout_icon)
        element.click()
        element = self.driver.find_element(*MainPageLocators.Signout_button)
        element.click()

    def click_Vehicle_rename(self):
        element = self.driver.find_element(*MainPageLocators.Vehicle_option)
        element.click()
        element = self.driver.find_element(*MainPageLocators.Vehicle_Vishal)
        element.click()
        element = self.driver.find_element(*MainPageLocators.Vehicle_setting)
        element.click()
        element = self.driver.find_element(*MainPageLocators.Vehicle_edit)
        element.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*MainPageLocators.Vehicle_rename).clear()
        self.driver.find_element(*MainPageLocators.Vehicle_rename).send_keys("Vishal")
        element = self.driver.find_element(*MainPageLocators.Vehicle_edit_save)
        element.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
