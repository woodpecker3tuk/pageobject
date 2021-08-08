from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.register import Register

class Login(BasePage):
    #扫码
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)