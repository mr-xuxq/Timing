#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure, time


class Test_modifyMessage():
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

    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))
    def test_modifyMessage(self):
        with allure.step('点击更多按钮'):
            self.page.more().click_more()
        with allure.step('点击进入个人主页'):
            self.page.more().click_person()

        with allure.step('点击修改资料按钮'):
            self.page.person_home().click_personInfo()
        with allure.step('点击更换照片'):
            self.page.edit_personal_info().click_changephoto()
        with allure.step('点击更换照片后返回'):
            self.page.edit_personal_info().click_return1()

        # with allure.step('点击选择照片'):

        #       self.page.edit_personal_info().click_chosephoto()
        # with allure.step('点击选取'):
        #
        #       self.page.edit_personal_info().click_selection()
        #
        with allure.step('点击姓名输入框'):
            self.page.edit_personal_info().click_nameContentBox()

        with allure.step('输入新的姓名'):
            self.page.edit_personal_info().input_newname(111111)
        # with allure.step('点击右上角确定按钮'):
        #     self.page.edit_personal_info().click_determine()
        # with allure.step('点击性别按钮'):
        #     self.page.edit_personal_info().click_gender()

        # with allure.step('点击选择性别完成按钮'):
        #         self.page.edit_personal_info().click_genderSubmit()
        # with allure.step('点击选择生日按钮'):
        #         self.page.edit_personal_info().click_birthday()


