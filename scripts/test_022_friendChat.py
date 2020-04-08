import time,pytest, allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('聊天页功能')
class Test_friendChat():

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

    # @allure.story('文字聊天')
    # def test_chatWord(self):
    #     with allure.step('进入消息页面'):
    #         self.page.message().click_messageBtn()
    #     with allure.step('滑动消息页面寻找第一个道友'):
    #         i = 0
    #         while i < 2:
    #             if self.page.message().check_messageFriend() == True:
    #                 break
    #             else:
    #                 self.page.message().swipeByMessage()
    #                 i += 1
    #     with allure.step('找到道友后点击channel进入聊天页面'):
    #         self.page.message().click_messageFriend()
    #     with allure.step('输入聊天消息并点击发送'):
    #         self.page.friend_chat().click_messageBox()
    #         self.page.friend_chat().input_messageBox("I am a message!")
    #         self.page.friend_chat().click_messageSend()
    #     with allure.step('校验结果：如果出现发送失败红点——>失败'):
    #         assert self.page.friend_chat().waitAndfind_failSend() == False
    #
    # @allure.story('图片聊天')
    # def test_chatImage(self):
    #     with allure.step('进入消息页面'):
    #         self.page.message().click_messageBtn()
    #     with allure.step('滑动消息页面寻找第一个道友'):
    #         i = 0
    #         while i < 2:
    #             if self.page.message().check_messageFriend() == True:
    #                 break
    #             else:
    #                 self.page.message().swipeByMessage()
    #                 i += 1
    #     with allure.step('找到道友后点击channel进入聊天页面'):
    #         self.page.message().click_messageFriend()
    #     with allure.step('点击聊天页面添加按钮'):
    #         self.page.friend_chat().click_chooseType()
    #         time.sleep(2)
    #     with allure.step('选择相册'):
    #         # 点击聊天页面【相册】按钮
    #         self.page.friend_chat().click_imageBtn()
    #     with allure.step('选择相册页面第一张图片并发送'):
    #         time.sleep(3)
    #         self.page.choose_image().click_chooseImage()
    #         self.page.choose_image().click_nextStep()
    #     with allure.step('校验结果：如果出现发送失败红点——>失败'):
    #         assert self.page.friend_chat().waitAndfind_failSend() == False

    @allure.story('视频聊天')
    def test_chatVideo(self):
        with allure.step('进入消息页面'):
            self.page.message().click_messageBtn()
        with allure.step('滑动消息页面寻找第一个道友'):
            i = 0
            while i < 2:
                if self.page.message().check_messageFriend() == True:
                    break
                else:
                    self.page.message().swipeByMessage()
                    i += 1
        with allure.step('找到道友后点击channel进入聊天页面'):
            self.page.message().click_messageFriend()
        with allure.step('点击聊天页面添加按钮'):
            self.page.friend_chat().click_chooseType()
            time.sleep(2)
        with allure.step('选择视频'):
            self.page.friend_chat().click_videoBtn()
        with allure.step('视频选择页选中一个视频并发送'):
            time.sleep(3)
            self.page.choose_video().click_chooseVideo()
        with allure.step('校验结果：如果出现发送失败红点——>失败'):
            assert self.page.friend_chat().waitAndfind_failSend() == False








