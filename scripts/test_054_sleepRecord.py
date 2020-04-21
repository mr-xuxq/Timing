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
        with allure.step('进入发布页面'):
            self.page.shouye().click_post()
            time.sleep(5)
        #学习计时页面用例能正常滑动，到了起床睡觉，滑动失败的概率很大，所以采用点击【+】，在发布页面选择【起床睡觉】按钮
        with allure.step('点击睡觉按钮，进入睡觉页面'):
            time.sleep(3)
            self.page.more().click_sleep()
            # 点击【睡觉actionbar】
            time.sleep(2)
            with allure.step('点击睡觉'):
                self.page.more().clickCoordinate_sleep()
                time.sleep(5)
            with allure.step('进入睡觉页面后关闭睡觉打卡弹窗，并点击起床'):
                self.page.timing().click_sleepingClose()
                time.sleep(2)
                self.page.timing().click_sleepingWake()
                time.sleep(3)
                self.driver.press_keycode(4)
                time.sleep(3)
                self.driver.press_keycode(4)
        with allure.step('判断是否成功起床'):
            #判断起床的断言需要修改
            assert self.page.shouye().waitAndFind() == True