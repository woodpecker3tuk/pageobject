from selenium.webdriver.common.by import By

from test_project.page.add_member import AddNumber
from test_project.page.base_page import BasePage
from test_project.page.contact_page import ContactPage

#主页面
class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def go_to_contect(self):
        return ContactPage(self.driver)

    def go_to_add_number(self):
        self.driver.find_element(By.CSS_SELECTOR,"[node-type='addmember']").click()
        return AddNumber(self.driver)





