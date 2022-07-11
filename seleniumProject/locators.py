from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    Login_BUTTON = (By.ID, 'submitLogin')
    User_name = (By.ID, "username")
    Password_value = (By.ID, "password")
    Signout_option = (By.XPATH, "//div[contains(@class, 'dropdown user-item')]")
    Signout_icon = (By.XPATH, "//div[normalize-space()='Log Out']")
    Signout_button = (By.XPATH, "//button[normalize-space()='Log Out']")
    Vehicle_option = (By.XPATH, "//div[contains(@class, 'vehicle-info')]")
    Vehicle_Vishal = (By.XPATH, "//div[contains(@title, 'Vishal')]")
    Vehicle_setting = (By.XPATH, "//div[normalize-space()='Vehicle Settings']")
    Vehicle_edit = (By.XPATH, "//div[@class='section vehicle-section']//button[@type='button'][normalize-space()='Edit']")
    Vehicle_rename = (By.XPATH, "//input[@id='mat-input-0']")
    Vehicle_edit_save = (By.XPATH, "//button[@class='btn-primary']")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
