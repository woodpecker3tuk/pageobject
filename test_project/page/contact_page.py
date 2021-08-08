#通讯录页面
from selenium.webdriver.common.by import By


from test_project.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_number(self):
        from test_project.page.add_member import AddNumber
        return AddNumber(self.driver)

    def get_number_list(self):
        self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")








