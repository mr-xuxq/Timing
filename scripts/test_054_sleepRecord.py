import time, allure
from Pages.timed_learning.timing_page import Timing
from Pages.personal_information.more_page import More
from Pages.page import Page
from base.base_driver import Base
#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
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
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击睡觉按钮，进入睡觉页面'):
            self.page.more().click_sleep()
            # 点击【睡觉actionbar】
            self.driver.tap([(329, 1969), (481, 2013)], 500)
            time.sleep(5)
            with allure.step('进入睡觉页面后关闭睡觉打卡弹窗，并点击起床'):
                while self.page.timing().waitAndfind(Timing.sleepingClose, 1) == True:
                    self.page.timing().click_timing(Timing.sleepingClose)
                    self.page.timing().click_timing(Timing.sleepingWake)
                    time.sleep(2)
                    self.driver.press_keycode(4)
        with allure.step('判断是否成功起床'):
            assert self.page.more().waitAndfind(More.sleepBtn, 1) == True
