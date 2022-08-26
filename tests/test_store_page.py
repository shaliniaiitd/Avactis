import pytest
import allure
from Selenium.Avactis_pytest.tests.test_base import BaseTest
from Selenium.Avactis_pytest.pages.store_page import StorePage
@pytest.mark.usefixtures("init_driver")
class TestStorePage():

    def test_a_title(self):
        self.store_page = StorePage(self.driver)

        title = self.store_page.get_title()
        assert(title == "Avactis Demo Store")

    def test_click_sign_in(self):
        self.store_page = StorePage(self.driver)
        self.sign_in_page = self.store_page.click_sign_in()
        assert(self.sign_in_page.get_title() == "Avactis Demo Store")
        return(self.sign_in_page)
