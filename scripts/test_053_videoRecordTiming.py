import time, allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('视频打卡功能')
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
        with allure.step('进入发布页面'):
            self.page.shouye().click_post()
            time.sleep(5)
<<<<<<< HEAD
=======
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMore()
            time.sleep(3)
            self.page.more().swipeByMore()
            time.sleep(1)
>>>>>>> 78ef5ac86c52608068f40fecb91b0e3097a77cf2
        with allure.step('点击视频打卡按钮，设定内容后开始'):
            self.page.more().click_video()
            self.page.timing().input_videoContentBox('This is videoTiming')
            time.sleep(3)
            self.page.timing().click_startVideoBtn()
            while self.page.timing().check_videoStartDialog() == True:
                self.page.timing().click_videoStartDialog()
                break
            self.page.timing().click_videoStartBtn()
            time.sleep(70)
            self.page.timing().click_timingEnd()
            self.page.timing().click_videoEndDialog()
        with allure.step('校验结果：视频打卡1min后判断计时是否正常结束'):
            assert self.page.timing().waitAndfind_videoSuccess()== True