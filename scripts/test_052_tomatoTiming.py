import time, allure
from Pages.timed_learning.timing_page import Timing
from Pages.personal_information.more_page import More
from Pages.page import Page
from base.base_driver import Base
#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
@allure.feature('番茄计时功能')
class Test_tomatoTiming():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 番茄计时
    def test_tomatoTiming(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击学习计时按钮，设定内容后开始'):
            self.page.more().click_timing()
            self.page.more().click_tomato()
            self.page.timing().input_ContentBox(Timing.tomatoContentBox, 'This is tomatoTiming')
            self.page.timing().click_timing(Timing.startTomatoBtn)
            #等待计时25min
            #time.sleep(1502)
            #assert self.page.timing().waitAndfind(Timing.timingEnd)
        assert self.page.timing().waitAndfind(Timing.timingEndConfirmLeft, 1) == True