import pytest
from selenium import webdriver

@pytest.fixture(params = ["chrome"],scope = 'class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
         web_driver = webdriver.Chrome()
    if request.param == "edge":
         web_driver = webdriver.Edge()

    request.cls.driver = web_driver
    yield webdriver
    web_driver.close()
