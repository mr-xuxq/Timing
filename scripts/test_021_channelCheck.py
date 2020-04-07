import allure
from Pages.page import Page
from base.base_driver import Base

#用feature说明产品需求
@allure.feature('消息页channel展示')
class Test_channelCheck():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(30)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()

    # #用story说明用户场景
    # @allure.story('Timing小书童channel')
    # def test_timingService(self):
    #     with allure.step('进入消息页面'):
    #         self.page.message().click_messageBtn()
    #     with allure.step('滑动寻找Timing小书童channel'):
    #         i = 0
    #         while i < 3:
    #             # 如果在规定时间找到该元素，则跳出循环
    #             if self.page.message().check_timingService()== True:
    #                 break
    #             # 如果没有找到，向上滑动页面继续找
    #             else:
    #                 self.page.message().swipeByMessage()
    #                 i += 1
    #     with allure.step('校验结果'):
    #         assert self.page.message().waitAndfind_timingService()== True

    @allure.story('互动通知channel')
    def test_interaction(self):
        with allure.step('进入消息页面'):
            self.page.message().click_messageBtn()
            i=0
            while i < 5000:
                self.page.message().click_interaction()
                self.driver.press_keycode(4)
                i+=1


        # with allure.step('滑动寻找互动通知'):
        #     i = 0
        #     while i < 3:
        #         if self.page.message().check_interaction()== True:
        #             break
        #         else:
        #             self.page.message().swipeByMessage()
        #             i += 1
        # with allure.step('校验结果'):
        #     assert self.page.message().waitAndfind_interaction()== True








