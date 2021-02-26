#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure,time

class Test_farmTime():
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

    def test_farmTimeLess(self):
        with allure.step('进入更多页'):
            self.page.more().click_more()
        with allure.step('点击自律工具'):
            self.page.timing().click_studyTools()
        with allure.step('点击农场学习'):
            self.page.timing().click_farmTiming()
        with allure.step('输入学习内容'):
            time.sleep(3)
            self.page.timing().input_learningTargetBox(12345)
        with allure.step('点击设置按钮'):
            self.page.timing().click_timeSettingBtn()
        with allure.step('设置学习时长'):
            time.sleep(3)
            self.page.more().swipeByTime()
        with allure.step('点击设置完成按钮'):
            self.page.timing().click_studySettingsuccessBtn()
        with allure.step('点击开始学习'):
            self.page.timing().click_startLearningBtn()
        with allure.step('点击结束'):
            self.page.farm_timing().click_farmTimeEndBtn()
        with allure.step('点击确定'):
            self.page.farm_timing().click_timingEndConfirmRight()
        with allure.step('点击后退'):
            self.page.timing().click_back()
        with allure.step('判断跳到更多页'):
            assert self.page.more().waitAndfind_more() == True

    def test_farmTimeEnough(self):
        with allure.step('进入更多页'):
            self.page.more().click_more()
        with allure.step('点击自律工具'):
            self.page.timing().click_studyTools()
        with allure.step('点击农场学习'):
            self.page.timing().click_farmTiming()
        with allure.step('输入学习内容'):
            time.sleep(3)
            self.page.timing().input_learningTargetBox(12345)
        with allure.step('点击设置按钮'):
            self.page.timing().click_timeSettingBtn()
        with allure.step('设置学习时长'):
            time.sleep(3)
            self.page.more().swipeByTime()
        with allure.step('点击设置完成按钮'):
            self.page.timing().click_studySettingsuccessBtn()
        with allure.step('点击开始学习'):
            self.page.timing().click_startLearningBtn()
        with allure.step('判断时间到了结束弹窗'):
            time.sleep(55)
        with allure.step('点击我知道了'):
            self.page.farm_timing().click_timingDialog()
        with allure.step('点击结束'):
            time.sleep(1)
            self.page.farm_timing().tapScreen(0.500,0.948)
        with allure.step('点击确定'):
            self.page.farm_timing().click_timingEndConfirmRight()
        with allure.step('判断跳转到完成页面'):
            assert self.page.farm_timing().check_timingEndSuccess() == True
