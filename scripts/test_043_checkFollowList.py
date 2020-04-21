import time, allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('关注列表检查')
class Test_CheckFollowList():

    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('')
    def test_checkFollowList(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('获取关注列表的人数'):
            number1 = self.page.more().get_followCount()
            temp1 = int(number1)
            #print(number1)
        with allure.step('点击进入首页'):
            time.sleep(2)
            self.page.shouye().click_shouye()
        with allure.step('点击一篇日记,进入详情页'):
            time.sleep(2)
            self.page.shouye().tapScreen(0.23,0.84)
        with allure.step('日记进详情页,点击关注'):
            time.sleep(3)
            self.page.daily().click_follow()
        with allure.step('点击返回,回到首页'):
            self.driver.press_keycode(4)
        with allure.step('点击进入更多页面'):
            time.sleep(3)
            self.page.more().click_more()
        with allure.step('下拉刷新更多页面'):
            time.sleep(5)
            self.page.more().swipeByRefresh()
        with allure.step('再次获取关注人数'):
            time.sleep(2)
            number2 = self.page.more().get_followCount()
            temp2 = int(number2) - 1
        with allure.step('判断关注人数变化是否正确'):
            assert self.page.more().compare_count(temp1,temp2) == True



