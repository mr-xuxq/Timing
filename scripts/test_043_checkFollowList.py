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

    @allure.story('关注一位陌生用户，查看用户数量变化是否正确')
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
            self.page.shouye().click_shouyeBtn()
        with allure.step('点击一篇日记,进入详情页'):
            time.sleep(2)
            self.driver.tap([(105,1550),(291,1628)],500)
        with allure.step('日记进详情页,点击关注'):
            self.page.daily().click_followBtn()
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
        assert self.page.more().compare_count(temp1,temp2) == True

    @allure.story('取消关注一位人数，查看用户数量变化是否正确')
    def test_checkFollowList(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('获取关注列表的人数'):
            number1 = self.page.more().get_followCount()
            temp1 = int(number1)
            # print(number1)
        with allure.step('进入我的关注页面'):
            self.page.more().click_followCount()
            time.sleep(2)
        with allure.step('点击已关注按钮，取消关注'):
            self.page.follow().cancel_followed()
            self.page.follow().cancelFollowedRight()
        with allure.step('返回更多页面'):
            self.driver.press_keycode(4)
            time.sleep(5)
            self.page.more().swipeByRefresh()
        with allure.step('再次获取关注人数'):
            time.sleep(2)
            number2 = self.page.more().get_followCount()
            temp2 = int(number2) + 1
        assert self.page.more().compare_count(temp1, temp2) == True





