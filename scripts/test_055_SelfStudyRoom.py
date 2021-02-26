# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 16:11
# @Author  : Geng
# @File    : test_055_SelfStudyRoom.py
#coding:utf-8
import time,allure,random
from Pages.page import Page
from base.base_driver import Base
#from base.base_analyze import analyze_file
import pandas as pd

class Test_changeNickname():
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

    #进入自习室免费区围观
    def test_SelfStudyRoom(self):
        with allure.step('点击自习室'):
            self.page.shouye().click_videoRoom()
        with allure.step('自习室列表页点击快速加入'):
            self.page.Free_zone().click_quickjoin()
        with allure.step('自习室座位页点击快速加入'):
            self.page.Free_study_room().click_quickjoin()

        with allure.step('检查是否跳到自习室房间'):
            result = self.page.Free_study_room().check_audience()
            if result == True:
                with allure.step('断言:成为观众'):
                    assert self.page.Free_study_room().check_zoom() == True
            # else:
            #     with allure.step('断言:成为房主'):

        #     time.sleep(2)
        # with allure.step('正式服数据库拿验证码'):
        #     captcha = pd.read_sql('select captcha FROM t_captcha WHERE phone = "' + str(phone) + '" order by postTime desc',engine)
        #     captcha = captcha.iloc[0, 0]
        # with allure.step('输入验证码'):
        #     self.page.login_phone_captcha().input_captcha(str(captcha))
        # with allure.step('点击完成'):
        #     self.page.login_phone_captcha().click_loginBtn()
        #     time.sleep(5)
        # with allure.step('点击更多按钮'):
        #     self.page.more().click_more()
        #     time.sleep(3)
        # with allure.step('进入个人主页'):
        #     self.page.more().click_person()
        #     time.sleep(1)
        # with allure.step('判断用户是否认证过'):
        #     if self.page.person_home().check_authenIcon() == False:
        #         with allure.step('点击修改资料'):
        #             self.page.person_home().click_personInfo()
        #             time.sleep(5)
        #         with allure.step('点击修改姓名'):
        #             self.page.edit_personal_info().tapScreen(0.5,0.377)
        #             time.sleep(1)
        #         with allure.step('修改姓名'):
        #             name = random.randint(1, 200000)
        #             self.page.name_info().input_nameBox(name)
        #             time.sleep(1)
        #         with allure.step('点击确定'):
        #             self.page.name_info().click_nameRight()
        #             time.sleep(1)
        #         with allure.step('点击后退'):
        #             self.page.edit_personal_info().click_back()
        #     else:
        #         pass
        # with allure.step('点击后退'):
        #     self.page.edit_personal_info().click_back()
        #     time.sleep(1)
        # with allure.step('点击设置按钮'):
        #     self.page.more().click_setting()
        # with allure.step('点击退出登录按钮'):
        #     self.page.setting().click_logout()
        # with allure.step('确定退出'):
        #     self.page.setting().click_confirmLogout()
        #     time.sleep(2)
        with allure.step('断言:进入房间成功'):
            assert self.page.login().check_loginByphone() == True


