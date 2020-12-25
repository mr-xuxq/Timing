#coding:utf-8
from Pages.page import Page
from base.base_driver import Base
import allure,time


class Test_studyTime():
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



    def test_studyTimeLess(self):
        with allure.step('计时不足一分钟点击结束'):
            with allure.step('更多页滑动到最底部'):
                self.page.more().click_more()
                time.sleep(3)
                self.page.more().swipeByMore()
                time.sleep(3)
            with allure.step('点击开始学习'):
                self.page.more().click_normalTiming()
            with allure.step('输入学习内容'):
                self.page.timing().input_studyContentBox(12345)
            with allure.step('点击设置按钮'):
                self.page.timing().click_studySettingBtn()
            with allure.step('设置学习时长'):
                time.sleep(3)
                self.page.more().swipeByTime()
            with allure.step('点击设置完成按钮'):
                self.page.timing().click_studySettingsuccessBtn()
            with allure.step('点击开始学习'):
                self.page.timing().click_startTimingBtn()
            with allure.step('点击停止学习'):
                self.page.timing().click_timingEnd()
            with allure.step('点击确定'):
                self.page.timing().click_timingEndConfirmRight()
            with allure.step('判断跳到更多页'):
                assert self.page.more().waitAndfind_more() == True



    def test_studyTimeEnough(self):
        with allure.step('计时一分钟提醒后点击结束'):
            with allure.step('更多页滑动到最底部'):
                self.page.more().click_more()
                time.sleep(3)
                self.page.more().swipeByMore()
                time.sleep(3)
            with allure.step('点击开始学习'):
                self.page.more().click_normalTiming()
            with allure.step('输入学习内容'):
                self.page.timing().input_studyContentBox(12345)
            with allure.step('点击设置按钮'):
                self.page.timing().click_studySettingBtn()
            with allure.step('设置学习时长'):
                time.sleep(3)
                self.page.more().swipeByTime()
            with allure.step('点击设置完成按钮'):
                self.page.timing().click_studySettingsuccessBtn()
            with allure.step('点击开始学习'):
                self.page.timing().click_startTimingBtn()
            with allure.step('判断时间到了结束弹窗'):
                time.sleep(50)
                assert self.page.timing().check_timingDialog() == True
            with allure.step('点击我知道了'):
                self.page.timing().click_timingDialog()
            with allure.step('点击结束'):
                self.page.timing().click_timingEnd()
            with allure.step('判断知道了弹窗'):
                result = self.page.timing().check_timingEndDialog()
                if result == True:
                    self.page.timing().click_timingEndDialog()
                else:
                    pass
            with allure.step('判断跳转到完成页面'):
                assert self.page.timing().waitAndfind_timingEndSuccess() == True



    def test_studyTimePause(self):
        with allure.step('计时一分钟暂停继续学习时点击结束'):
            with allure.step('更多页滑动到最底部'):
                self.page.more().click_more()
                time.sleep(3)
                self.page.more().swipeByMore()
                time.sleep(3)
            with allure.step('点击开始学习'):
                self.page.more().click_normalTiming()
            with allure.step('输入学习内容'):
                self.page.timing().input_studyContentBox(12345)
            with allure.step('点击设置按钮'):
                self.page.timing().click_studySettingBtn()
            with allure.step('设置学习时长'):
                time.sleep(3)
                self.page.more().swipeByTime()
            with allure.step('点击设置完成按钮'):
                self.page.timing().click_studySettingsuccessBtn()
            with allure.step('点击开始学习'):
                self.page.timing().click_startTimingBtn()
            with allure.step('暂停学习'):
                self.page.timing().click_timingPause()
            with allure.step('点击继续'):
                self.page.timing().click_timingContinue()
            with allure.step('判断时间到了结束弹窗'):
                time.sleep(50)
                assert self.page.timing().check_timingDialog() == True
            with allure.step('点击我知道了'):
                self.page.timing().click_timingDialog()
            with allure.step('点击再学30分钟'):
                self.page.timing().click_timingAgain()
            with allure.step('点击结束'):
                self.page.timing().click_timingEnd()
            with allure.step('等待弹窗'):
                assert self.page.timing().waitAndfind_timingEndConfirmLeft()==True
            with allure.step('点击确定'):
                self.page.timing().click_timingEndConfirmRight()
            with allure.step('判断跳转到完成页面'):
                assert self.page.timing().waitAndfind_timingEndSuccess() == True


    def test_studyTimeTogether(self):
        with allure.step('计时一分钟邀请别人一起学习'):
            with allure.step('更多页滑动到最底部'):
                self.page.more().click_more()
                time.sleep(3)
                self.page.more().swipeByMore()
                time.sleep(3)
            with allure.step('点击开始学习'):
                self.page.more().click_normalTiming()
            with allure.step('输入学习内容'):
                self.page.timing().input_studyContentBox(12345)
            with allure.step('点击设置按钮'):
                self.page.timing().click_studySettingBtn()
            with allure.step('设置学习时长'):
                time.sleep(3)
                self.page.more().swipeByTime()
            with allure.step('点击设置完成按钮'):
                self.page.timing().click_studySettingsuccessBtn()
            with allure.step('点击开始学习'):
                self.page.timing().click_startTimingBtn()
            with allure.step('点击邀请'):
                self.page.timing().click_studyTogetherBtn()
            with allure.step('点击邀请的人'):
                time.sleep(3)
                self.page.timing().tapOperat(0.4, 0.402)
            with allure.step('点击发送'):
                self.page.timing().click_studyTogetherForwardBtn()
                time.sleep(3)
            with allure.step('点击关闭按钮'):
                self.page.timing().click_studyCloseBtn()
            with allure.step('点击确定'):
                self.page.timing().click_timingEndConfirmRight()
            with allure.step('点击消息页'):
                self.page.message().click_messageBtn()
            with allure.step('点击计时'):
                if self.page.message().check_timeFloat()== True:
                    self.page.message().click_timeFloat()
                else: pass
            with allure.step('关闭计时'):
                self.page.timing().click_timingEnd()
            with allure.step('等待弹窗'):
                assert self.page.timing().waitAndfind_timingEndConfirmLeft()==True
            with allure.step('点击确定'):
                self.page.timing().click_timingEndConfirmRight()
            with allure.step('判断跳到更多页'):
                assert self.page.more().waitAndfind_more() == True

    def test_studyTimeDiscuss(self):
        with allure.step('讨论'):
            with allure.step('更多页滑动到最底部'):
                self.page.more().click_more()
                time.sleep(3)
                self.page.more().swipeByMore()
                time.sleep(3)
            with allure.step('点击开始学习'):
                self.page.more().click_normalTiming()
            with allure.step('输入学习内容'):
                self.page.timing().input_studyContentBox(12345)
            with allure.step('点击设置按钮'):
                self.page.timing().click_studySettingBtn()
            with allure.step('设置学习时长'):
                time.sleep(3)
                self.page.more().swipeByTime()
            with allure.step('点击设置完成按钮'):
                self.page.timing().click_studySettingsuccessBtn()
            with allure.step('点击开始学习'):
                self.page.timing().click_startTimingBtn()
            with allure.step('点击讨论'):
                self.page.timing().click_studyDiscussBtn()

            with allure.step('弹出键盘'):
                self.page.timing().click_studyDiscussContentBox()
                time.sleep(3)
            with allure.step('讨论输入框输入内容'):
                self.page.timing().input_studyDiscussContentBox(12345)
            with allure.step('点击发送'):
                self.page.timing().click_studyDiscussSendBtn()
            with allure.step('判断有没有讨论的内容'):
                self.page.timing().check_studyDiscussContent()
            with allure.step('点击关闭按钮'):
                self.page.timing().click_studyCloseBtn()
            with allure.step('点击确定'):
                self.page.timing().click_timingEndConfirmRight()
            with allure.step('点击消息页'):
                self.page.message().click_messageBtn()
            with allure.step('点击计时'):
                if self.page.message().check_timeFloat()== True:
                    self.page.message().click_timeFloat()
                else:
                    pass
            with allure.step('关闭计时'):
                self.page.timing().click_timingEnd()
            with allure.step('等待弹窗'):
                assert self.page.timing().waitAndfind_timingEndConfirmLeft()==True
            with allure.step('点击确定'):
                self.page.timing().click_timingEndConfirmRight()
            with allure.step('判断跳到更多页'):
                assert self.page.more().waitAndfind_more() == True