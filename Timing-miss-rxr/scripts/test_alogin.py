import allure,pytest
from Pages.page import Page
from base.base_driver import Base
from Pages.login_phone_pwd_page import Login_phone_pwd
from Pages.main_page import Main
class Test_login():

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

    #手机号密码登录测试用例
    def test_loginByphone(self):
        self.page.login().click_phone_login()
        self.page.login_phone().click_password_login()
        self.page.login_phone_pwd().input_home_phone(Login_phone_pwd.phone)
        self.page.login_phone_pwd().input_home_pwh(Login_phone_pwd.password)
        self.page.login_phone_pwd().back()
        self.page.login_phone_pwd().click_home_login()
        #断言
        assert self.page.main().waitAndfind(Main.postBtn,20) == True

    # if __name__ == '__main__':
    #     # 执行，指定执行测试模块_demo1, 测试模块_demo2两个模块，同时指定执行的用例优先级为critical,blocker
    #     pytest.main(['--allure_stories=测试模块_demo1, 测试模块_demo2', '--allure_severities=critical, blocker'])