#添加人员页面
from time import sleep
from selenium.webdriver.common.by import By
from test_project.page.base_page import BasePage
from test_project.page.contact_page import ContactPage

class AddNumber(BasePage):
    # _username = (By.ID,"username")
    def add_number(self):
        # self.find(*self._username).send_keys("行行行")
        self.driver.find_element(By.ID,"username").send_keys("伊泽瑞尔")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("236")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("18329433226")
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        sleep(3)
        return ContactPage(self.driver)

    # def get_phone_error_message(self):
    #     return self.driver.find_element(By.CSS_SELECTOR,".ww_inputWithTips_WirhE")






















