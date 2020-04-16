import time,pytest, allure
from Pages.page import Page
from base.base_driver import Base
from appium.webdriver.common.touch_action import TouchAction

@allure.feature('群组聊天功能')
class Test_teamChat():

    #setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
    #放一些准备的工作，或者准备一些测试数据。
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
        self.action = TouchAction(self.driver)

    #tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
    #当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
    def teardown(self):
        self.driver.quit()

    @allure.story('文字聊天')
    def test_teamChatWord(self):
        self.page.message().click_messageBtn()
        #判断当前的消息页面有没有有没有群组，没有群组时就直接pass
        # if self.page.message().check_messageTeam() == False:
        #     with allure.step('当前页面没有群组'):
        #         pass
        # else:
        # with allure.step('当有道友动态时，滑动页面'):
        #     self.page.message().check_friendDynamic()
        with allure.step('点击小书童后返回至消息页面，使小书童不置顶'):
            self.page.message().click_timingService()
            time.sleep(2)
            self.driver.press_keycode(4)
        with allure.step('找到群组后使channel置顶'):
            e1 = self.driver.find_element_by_id("com.huiian.timing:id/team_type_iv")
            self.action.long_press(e1, None, None, 3000).perform()
            time.sleep(2)
            self.page.message().click_setTop()
            time.sleep(1)
            with allure.step('点击channel进入聊天页面'):
                self.page.message().click_messageTeam()
                time.sleep(2)
            with allure.step('发送聊天消息'):
                self.page.friend_chat().click_messageBox()
                self.page.friend_chat().input_messageBox("I am a message!")
                self.page.friend_chat().click_messageSend()
                time.sleep(5)
            self.page.friend_chat().click_backTeam()
            count = self.driver.find_element_by_id('com.huiian.timing:id/friend_msg_content_tv').text
            with allure.step('校验结果：若发送成功，消息页会显示最新消息'):
                assert count == "I am a message!"

    @allure.story('图片聊天')
    def test_chatImage(self):
        self.page.message().click_messageBtn()
        with allure.step('点击聊天页面添加按钮'):
            self.page.message().click_messageTeam()
            time.sleep(2)
            self.page.friend_chat().click_chooseType()
            time.sleep(1)
        with allure.step('选择相册'):
            # 点击聊天页面【相册】按钮
            self.page.friend_chat().click_imageBtn()
        with allure.step('选择相册页面第一张图片并发送'):
            time.sleep(3)
            self.page.choose_image().click_chooseImage()
            self.page.choose_image().click_nextStep()
            time.sleep(5)
            self.page.friend_chat().click_backTeam()
            self.page.friend_chat().click_backTeam()
            count = self.driver.find_element_by_id('com.huiian.timing:id/friend_msg_content_tv').text
        with allure.step('校验结果：若发送成功，消息页会显示最新图片'):
            assert count == "[图片]"

    @allure.story('视频聊天')
    def test_chatVideo(self):
        self.page.message().click_messageBtn()
        with allure.step('点击聊天页面添加按钮'):
            self.page.message().click_messageTeam()
            time.sleep(2)
            self.page.friend_chat().click_chooseType()
            time.sleep(1)
        with allure.step('选择视频'):
            self.page.friend_chat().click_videoBtn()
        with allure.step('视频选择页选中一个视频并发送'):
            time.sleep(3)
            self.page.choose_video().click_chooseVideo()
            time.sleep(5)
            self.page.friend_chat().click_backTeam()
            self.page.friend_chat().click_backTeam()
            count = self.driver.find_element_by_id('com.huiian.timing:id/friend_msg_content_tv').text
            with allure.step('取消群组channel置顶'):
                e1 = self.driver.find_element_by_id("com.huiian.timing:id/team_type_iv")
                self.action.long_press(e1, None, None, 3000).perform()
                time.sleep(2)
                self.page.message().click_setTop()
                time.sleep(2)
        with allure.step('校验结果：若发送成功，消息页会显示最新视频'):
            assert count == "[视频]"