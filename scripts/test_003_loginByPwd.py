#coding:utf-8
from Pages.page import Page
from base.base_driver import Base

sourse = []
phone = 10000000100                                         # 登录手机
pwd = 111111                                                # 登录密码

class Test_loginByPwd():
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
    def test_loginByPwd(self):
        self.page.login().click_phone_login()
        self.page.login_phone().click_loginByPwd()
        self.page.login_phone_pwd().input_phone(str(phone))
        self.page.login_phone_pwd().input_pwd(str(pwd))
        self.page.login_phone_pwd().back()
        self.page.login_phone_pwd().click_loginBtn()
        #断言
        #consult = Test_loginByPwd.findItem(self,target)
        assert self.page.login_phone_pwd().waitAndFind() == True

    # def test_logout(self):
    #     self.page.setting().click_more()
    #     self.page.setting().click_setting()
    #     self.page.setting().click_logout()
    #     self.page.setting().click_confirmLogout()
    #     assert self.page.setting().findLogin() == True






