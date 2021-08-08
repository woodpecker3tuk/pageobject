#添加人员页面
from selenium.webdriver.common.by import By

from test_project.page.base_page import BasePage
from test_project.page.contact_page import ContactPage


class AddNumber(BasePage):
    def add_number(self):
        self.driver.find_element(By.ID,"username").send_keys("皮皮虾")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("3")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("18329432123")
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

        return ContactPage()






















