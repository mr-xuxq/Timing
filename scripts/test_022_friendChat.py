import time,pytest, allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('聊天页功能')
class Test_friendChat():
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    # def test_skip_1(self):
    #     # 当消息页面没有道友时，跳过执行以下测试用例
    #     self.page.message().click_message(Message.messageBtn)
    #     if self.page.message().waitAndfind(Message.messageFriend, 1)== False:
    #         pytest.skip("test_chatWord")
    #         pytest.skip("test_chatImage")
    #         pytest.skip("test_chatVideo")
    #     else:
    #         # @不执行下面用例时，加上pytest.mark.skip(reason="不想执行的理由")
    @allure.story('文字聊天')
    def test_chatWord(self):
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
        with allure.step('输入聊天消息并点击发送'):
            self.page.friend_chat().input_messageBox("I am a message!")
            self.page.friend_chat().click_messageSend()
        with allure.step('校验结果：如果出现发送失败红点——>失败'):
            assert self.page.friend_chat().waitAndfind_failSend() == False

    @allure.story('图片聊天')
    def test_chatImage(self):
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
            # self.driver.tap([(998, 2272), (1000, 2282)], 500)
            self.page.friend_chat().click_chooseType()
        with allure.step('选择相册'):
            # 点击聊天页面【相册】按钮
            self.driver.tap([(140, 1860), (141, 1862)], 500)
        with allure.step('选择相册页面第一张图片并发送'):
            self.page.choose_image().click_chooseImage()
            self.page.choose_image().click_nextStep()
        with allure.step('校验结果：如果出现发送失败红点——>失败'):
            assert self.page.friend_chat().waitAndfind_failSend() == False

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
            # self.driver.tap([(998, 2272), (1000, 2282)], 500)
            self.page.friend_chat().click_chooseType()
        with allure.step('选择视频'):
            self.driver.tap([(387, 1865), (388, 1866)], 500)
        with allure.step('视频选择页选中一个视频并发送'):
            self.page.choose_video().click_chooseVideo()
        with allure.step('校验结果：如果出现发送失败红点——>失败'):
            assert self.page.friend_chat().waitAndfind_failSend() == False








