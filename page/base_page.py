from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    #初始化
    def __init__(self,driver:WebDriver = None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,location):
        return self._driver.find_element(by,location)

