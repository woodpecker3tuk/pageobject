#通讯录页面
from selenium.webdriver.common.by import By
from test_project.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_number(self):
        from test_project.page.add_member import AddNumber
        return AddNumber(self.driver)

    def get_number_list(self):
        name_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        list1=[]
        for name in name_list:
            list1.append(name.text)
        return list1







