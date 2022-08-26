import pytest
from Selenium.Avactis_pytest.Config.config import TestData as TD

@pytest.mark.usefixtures("init_driver")
class BaseTest():
    def __init__(self):

        #test_data = TD.data
        pass