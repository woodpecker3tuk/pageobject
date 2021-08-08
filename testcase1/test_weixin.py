import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class TestDemo1():
    def setup_method(self,method):
        #复用浏览器
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        #隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()

    def test_contact(self):
        sleep(2)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID,"menu_contacts").click()

    def test_cookie(self):

        #获取cookie
        #需要先复用浏览器，获取需要的登录之类的数据后，再获取
        cookie = self.driver.get_cookies()
        print(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_cookie1(self):
        #shelve小型的数据库，对象持久化保存方法，
        db = shelve.open("mydb/logincookies")
        # cookies = ["#此处为具体的cookie值"]
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        #需要先访问需要访问的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID,"menu_contacts").click()

    def test_importcontact(self):

        # shelve小型的数据库，对象持久化保存方法，
        db = shelve.open("mydb/logincookies")
        # cookies = ["#此处为具体的cookie值"]
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        # 需要先访问需要访问的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys("#此处为具体的文件路径")
        #断言
        assert  "#具体的文件名" == self.driver.find_element(By.ID,"upload_file_name").text
        sleep(3)








