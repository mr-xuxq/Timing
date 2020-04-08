import time, allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('睡觉后起床功能')
class Test_sleepRecord():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('睡觉后再起床操作')
    def test_sleepRecord(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMore()
            time.sleep(5)
        with allure.step('点击睡觉按钮，进入睡觉页面'):
            self.page.more().click_sleep()
            # 点击【睡觉actionbar】
            self.driver.tap([(329, 1969), (481, 2013)], 500)
            time.sleep(5)
            with allure.step('进入睡觉页面后关闭睡觉打卡弹窗，并点击起床'):
                self.page.timing().click_sleepingClose()
                self.page.timing().click_sleepingWake()
                self.driver.press_keycode(4)
        with allure.step('判断是否成功起床'):
            assert self.page.more().waitAndfind_sleepBtn()== True
