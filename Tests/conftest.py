import pytest
from selenium import webdriver
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome"],scope="class")
def test_setup(request):
    if request.param == "chrome":
        service = Service(executable_path=TestData.driver_path)
        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(service=service, options=options)
        #web_driver = webdriver.Chrome(executable_path=)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    yield
    web_driver.close()
    web_driver.quit()
    print("Test completed")

