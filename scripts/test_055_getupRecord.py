import time, allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('起床功能')
class Test_getupRecord():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('起床操作')
    def test_getupRecord(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMore()
            time.sleep(3)
        with allure.step('点击起床，关闭起床打卡弹窗'):
            self.page.more().click_sleep()
            #点击【起床】按钮
            self.driver.tap([(355, 1866), (456, 1900)], 500)
            # 分享弹窗不能被定位，点击返回
            self.driver.press_keycode(4)
        with allure.step('判断是否成功起床'):
            assert self.page.more().waitAndfind_sleepBtn() == True