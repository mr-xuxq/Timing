#！/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xinlan time:2021/1/15
from Pages.page import Page
from base.base_driver import Base
import allure,time
sourse = []

class Test_personalHomepage():
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
    def test_personalHomepage(self):
        with allure.step('点击更多按钮'):
            self.page.share_personal().click_more()
        with allure.step('点击进入个人主页'):
            self.page.share_personal().click_personalinfo()
        with allure.step('点击timingID'):
            self.page.share_personal().click_timingID()

        with allure.step('点击右上角分享个人主页'):
            self.page.share_personal().click_share()
        with allure.step('点击分享至微信好友'):
            self.page.share_personal().click_wechatfriends()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        # with allure.step('点击右上角分享个人主页'):
        #     self.page.share_personal().click_share()
        # with allure.step('点击分享至朋友圈'):
        #     self.page.share_personal().click_wechatmoments()
        # with allure.step('点击返回'):
        #     self.driver.press_keycode(4)
        # with allure.step('点击右上角分享个人主页'):
        #     self.page.share_personal().click_share()
        # with allure.step('点击分享至QQ空间'):
        #     self.page.share_personal().click_QQzone()
        # with allure.step('点击返回'):
        #     self.driver.press_keycode(4)
        with allure.step('点击右上角分享个人主页'):
            self.page.share_personal().click_share()
        with allure.step('点击分享至QQ好友'):
            self.page.share_personal().click_QQfriends()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        with allure.step('点击右上角分享个人主页'):
            self.page.share_personal().click_share()
        with allure.step('点击分享至微博'):
            self.page.share_personal().click_weibo()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        with allure.step('点击保存'):
            time.sleep(3)
            self.page.post_content().tapOperat(0.669, 0.592)
        with allure.step('点击右上角分享个人主页'):
            self.page.share_personal().click_share()
        with allure.step('点击分享至最近聊天'):
            self.page.share_personal().click_recentchat()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        # with allure.step('点击返回到个人主页'):
        #     self.page.share_personal().click_returnpersonal()
        with allure.step('点击我的二维码'):
            self.page.share_personal().click_MyQR_code()
        with allure.step('点击复制timingID'):
            self.page.share_personal().click_copyID()
        with allure.step('点击分享二维码名片'):
            self.page.share_personal().click_shareQR_code_card()
        with allure.step('点击分享到微信'):
            self.page.share_personal().click_share_weixin()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        # with allure.step('点击分享二维码名片'):
        #     self.page.share_personal().click_shareQR_code_card()
        # with allure.step('点击分享到朋友圈'):
        #     self.page.share_personal().click_friendsquan()
        # with allure.step('点击返回'):
        #     self.driver.press_keycode(4)
        with allure.step('点击分享二维码名片'):
            self.page.share_personal().click_shareQR_code_card()
        with allure.step('点击分享到QQ'):
            self.page.share_personal().click_share_qq()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        with allure.step('点击分享二维码名片'):
            self.page.share_personal().click_shareQR_code_card()
        with allure.step('点击分享到微博'):
            self.page.share_personal().click_share_weibo()
        with allure.step('点击返回'):
            self.driver.press_keycode(4)
        with allure.step('点击保存'):
            time.sleep(3)
            self.page.post_content().tapOperat(0.669, 0.592)
        with allure.step('点击分享二维码名片'):
            self.page.share_personal().click_shareQR_code_card()
        with allure.step('点击保存图片'):
            self.page.share_personal().click_savepicture()
        with allure.step('点击分享二维码名片'):
            self.page.share_personal().click_shareQR_code_card()
        with allure.step('点击取消'):
            self.page.share_personal().click_cancel()
        with allure.step('点击返回'):
            self.page.share_personal().click_returnback()
