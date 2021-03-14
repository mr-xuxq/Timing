#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure,time

class Test_getup_sleep():
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

    def test_sleep(self):
        with allure.step('进入更多页'):
            self.page.shouye().click_mainMoreBtn()
        with allure.step('点击起床睡觉'):
            time.sleep(2)
            self.page.more().click_getupAndSleepBtn()
        with allure.step('点击睡觉按钮'):
            self.page.getup_sleep().tapScreen(0.5,0.85)
        with allure.step('判断是否生成睡觉卡片'):
            assert self.page.getup_sleep().check_sleepCard() == True

    def test_getup(self):
        with allure.step('点击起床按钮'):
            self.page.getup_sleep().click_sleepAndGetupBtn()
        with allure.step('判断是否生成起床卡片'):
            assert self.page.getup_sleep().check_getupCard() == True
