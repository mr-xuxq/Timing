import time, allure
from Pages.timing_page import Timing
from Pages.more_page import More
from Pages.page import Page
from base.base_driver import Base
#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
@allure.feature('计时功能')
class Test_videoRecordTiming():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

        # 如果想让一条用例执行两次，在用例上方加上以下代码
        # @pytest.mark.repeat(2)

    @allure.story('视频打卡操作')
    def test_videoRecordTiming(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击视频打卡按钮，设定内容后开始'):
            self.page.more().click_more(More.videoBtn)
            self.page.timing().input_ContentBox(Timing.videoContentBox, 'This is videoTiming')
            time.sleep(3)
            self.page.timing().click_timing(Timing.startVideoBtn)
            while self.page.timing().waitAndfind(Timing.videoStartDialog, 1) == True:
                self.page.timing().click_more(Timing.videoStartDialog)
                break
            self.page.timing().click_timing(Timing.videoStartBtn)
            time.sleep(70)
            self.page.timing().click_timing(Timing.timingEnd)
            self.page.timing().click_timing(Timing.videoEndDialog)
        with allure.step('校验结果：视频打卡1min后判断计时是否正常结束'):
            assert self.page.timing().waitAndfind(Timing.videoSuccess, 1) == True