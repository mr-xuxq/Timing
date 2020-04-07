#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure,time
sourse = []


class Test_loginByQQ():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))
    # QQ登录测试用例
    def test_loginByQQ(self):
        with allure.step('点击QQ登录'):
            self.page.login().click_QQ_login()
            time.sleep(5)
        with allure.step('点击qq授权'):
            self.page.login().click_QQ_agree()
        with allure.step('断言:登录成功'):
            assert self.page.login().waitAndFind() == True

    def test_logout(self):
        with allure.step('点击更多按钮'):
            self.page.more().click_more()
        with allure.step('点击设置按钮'):
            self.page.more().click_setting()
        with allure.step('点击退出登录按钮'):
            self.page.setting().click_logout()
        with allure.step('确定退出'):
            self.page.setting().click_confirmLogout()
        with allure.step('断言:退出登录成功'):
            assert self.page.setting().findLogin() == True







