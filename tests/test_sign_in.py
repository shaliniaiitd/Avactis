import pytest
from Selenium.Avactis_pytest.pages.store_page import StorePage
from Selenium.Avactis_pytest.pages.sign_in_page  import SignInPage
from Selenium.Avactis_pytest.tests.test_store_page import TestStorePage
from Selenium.Avactis_pytest.Config.config import TestData as TD
from ddt import data, unpack

@pytest.mark.usefixtures("init_driver")
class TestSignIn():

     def test_sign_in(self):
         for dt in TD.data:
            print(dt[0], dt[1])
            self.store_page = StorePage(self.driver)
            self.sign_in_page = self.store_page.click_sign_in()
            #self.sign_in_page = TestStorePage().test_click_sign_in()
            self.sign_in_page.click_sign_in(dt[0],dt[1])

    #def test_register(self):
     #   self.sign_in_page.click_register()
        #time.sleep(10)

