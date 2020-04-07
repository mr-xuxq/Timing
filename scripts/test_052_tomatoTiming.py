import time, allure
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

    # 番茄计时，不足25min
    def test_tomatoTiming(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMore()
        with allure.step('点击学习计时按钮，设定内容后开始'):
            self.page.more().click_timing()
            self.page.more().click_tomato()
            self.page.timing().input_tomatoContentBox('This is tomatoTiming')
            self.page.timing().click_startTomatoBtn()
        with allure.step('判断能否正常进入番茄计时页面'):
            assert self.page.timing().waitAndfind_timingEndConfirmLeft() == True
            assert self.page.timing().waitAndfind_timingEndConfirmLeft() == True
