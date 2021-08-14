from test_project.page.main_page import MainPage


class TestAddNumber:
    def setup_class(self):
        self.main = MainPage()
    def test_add_number(self):
        # self.main = MainPage()
        #   1,跳转到添加成员 2，添加成员
        print(self.main)
        self.main.go_to_add_number().add_number()
        # result = self.main.go_to_add_number().add_number().get_number_list()
        # assert "伊泽瑞尔" in result
    def test_contact_add_number(self):
        #   1,跳转到通讯录页面 2，跳转到添加成员 3，添加成员
        self.main.go_to_contect().go_to_add_number().add_number()

    def teardown(self):
        self.main.driver.quit()












