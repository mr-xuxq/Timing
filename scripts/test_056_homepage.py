# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 20:19
# @Author  : Geng
# @File    : test_056_homepage.py
import time,allure,random
from Pages.page import Page
from base.base_driver import Base
#from base.base_analyze import analyze_file
import pandas as pd

class Test_shouye():
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

    #进入首页
    def test_homepage(self):
        with allure.step('点击搜索框'):
            self.page.shouye().click_search()
        with allure.step('检查是否有进入搜索页'):
            assert self.page.Help_home().check_manlist() == True
            self.driver.press_keycode(4)

        while self.page.shouye().check_live() == False:
            self.page.shouye().swipeUp()
        self.page.shouye().click_live()
        with allure.step('检查是否有进入live直播间'):
            assert self.page.Help_home().check_picture() == True
        time.sleep(3)
        self.driver.press_keycode(4)

        while self.page.shouye().check_tang_video() == False:
            self.page.shouye().swipeUp()
        self.page.shouye().click_tang_video()
        with allure.step('检查是否有进入汤视频列表页'):
            assert self.page.Help_home().check_icon() == True
        time.sleep(3)
        self.driver.press_keycode(4)

        while self.page.shouye().check_topic() == False:
            self.page.shouye().swipeUp()
        self.page.shouye().click_topic()
        with allure.step('检查是否有进入汤视频列表页'):
            assert self.page.Help_home().check_participationtopics() == True
        time.sleep(3)
        self.driver.press_keycode(4)






