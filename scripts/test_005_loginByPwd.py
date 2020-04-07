#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure
sourse = []
phone = 10000000403                                         # 登录手机
pwd = 111111                                                # 登录密码

class Test_loginByPwd():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))
    # 验证码登录测试用例
    def test_loginByPwd(self):
        with allure.step('点击手机号登录'):
            self.page.login().click_phone_login()
        with allure.step('点击密码登录'):
            self.page.login_phone().click_loginByPwd()
        with allure.step('输入手机号'):
            self.page.login_phone_pwd().input_phone(str(phone))
        with allure.step('输入密码'):
            self.page.login_phone_pwd().input_pwd(str(pwd))
        with allure.step('关闭小键盘'):
            self.page.login_phone_pwd().back()
        with allure.step('点击登录按钮'):
            self.page.login_phone_pwd().click_loginBtn()
        with allure.step('断言:登录成功'):
            assert self.page.login().waitAndFind() == True







