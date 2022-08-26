from selenium.webdriver.common.by import By

from Selenium.Avactis_pytest.pages.sign_in_page import SignInPage
from Selenium.Avactis_pytest.pages.base_page import BasePage
from Selenium.Avactis_pytest.Config.config import TestData as TD

class StorePage(BasePage):

    def __init__(self, driver):
            super().__init__(driver)
            self.driver.get(TD.url)

            self.sign_in = (By.LINK_TEXT, "Sign In")  # this is a locator, type is tuple

    def click_sign_in(self):
        self.do_click(self.sign_in)
        #self.driver.find_element(*self.sign_in).click()
        signin_page = SignInPage(self.driver)
        return signin_page
