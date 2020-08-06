#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure,time
sourse = []

class Test_loginByQQ():
    #setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
    #放一些准备的工作，或者准备一些测试数据。
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    #tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
    #当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
    def teardown(self):
        self.driver.quit()
    #判断元素是否在当前页面内
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))
    #手机号密码登录测试用例
    def test_loginByQQ(self):
        with allure.step('点击QQ登录'):
            self.page.login().click_QQ_login()
            time.sleep(5)
        with allure.step('点击qq授权'):
            self.page.login().click_QQ_agree()
            time.sleep(5)
        with allure.step('检查是否跳到首页'):
            result = self.page.shouye().check_shouye()
            if result == True:
                with allure.step('断言:登录成功'):
                    assert self.page.login().check_target() == True
            else:
                with allure.step('用户未绑定手机，用例结束'):
                    self.page.banding_phone().click_closeBtn()


    def test_logout(self):
        with allure.step('检测登陆状态'):
            result = self.page.shouye().check_shouye()
            if result == True:
                with allure.step('点击更多按钮'):
                    self.page.more().click_more()
                    time.sleep(3)
                with allure.step('点击设置按钮'):
                    self.page.more().click_setting()
                with allure.step('点击退出登录按钮'):
                    self.page.setting().click_logout()
                with allure.step('确定退出'):
                    self.page.setting().click_confirmLogout()
                    time.sleep(2)
                with allure.step('断言:退出登录成功'):
                    assert self.page.setting().check_target() == True
            else:
                with allure.step('处于未登录状态，用例结束'):
                    pass






