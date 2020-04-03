import time, allure
from Pages.timing_page import Timing
from Pages.more_page import More
from Pages.page import Page
from base.base_driver import Base
#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
@allure.feature('计时功能')
class Test_timing():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('学习计时操作')
    def test_timing(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击学习计时按钮，设定内容后开始'):
            self.page.more().click_more(More.timingBtn)
            self.page.timing().input_ContentBox(Timing.studyContentBox, 'This is Timing')
            self.page.timing().click_timing(Timing.studySettingBtn)
            time.sleep(5)
            #滑动选择1min
            self.page.more().swipeByMy(0.6, 0.8, 0.6, 0.75, 150)
            self.page.timing().click_timing(Timing.studySettingsuccessBtn)
            self.page.timing().click_timing(Timing.startTimingBtn)
            time.sleep(62)
        with allure.step('校验结果：计时1min后关闭计时的后续操作执行后判断计时是否正常结束'):
            if self.page.timing().waitAndfind(Timing.timingDialog,1) == True:
                self.page.timing().click_timing(Timing.timingDialog)
                self.page.timing().click_timing(Timing.timingEnd)
            else:
                self.page.timing().click_timing(Timing.timingEnd)
            if self.page.timing().waitAndfind(Timing.timingEndDialog,1) == True:
                self.page.timing().click_timing(Timing.timingEndDialog)
            else:
                assert self.page.timing().waitAndfind(Timing.timingEndSuccess,1) == True

    #番茄计时
    def test_tomatoTiming(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击学习计时按钮，设定内容后开始'):
            self.page.more().click_more(More.timingBtn)
            self.page.timing().input_ContentBox(Timing.tomatoContentBox, 'This is tomatoTiming')
            self.page.timing().click_timing(Timing.startTomatoBtn)
        assert self.page.timing().waitAndfind(Timing.timingEnd,1) == True

    #如果想让一条用例执行两次，在用例上方加上以下代码
    #@pytest.mark.repeat(2)
    @allure.story('视频打卡操作')
    def test_video(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击视频打卡按钮，设定内容后开始'):
            self.page.more().click_more(More.videoBtn)
            self.page.timing().input_ContentBox(Timing.videoContentBox,'This is videoTiming')
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
            assert self.page.timing().waitAndfind(Timing.videoSuccess,1) == True

    @allure.story('睡觉后再起床操作')
    def test_sleep(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击睡觉按钮，进入睡觉页面'):
            self.page.more().click_more(More.sleepBtn)
            #点击【睡觉actionbar】
            self.driver.tap([(329, 1969), (481, 2013)], 500)
            time.sleep(5)
            with allure.step('进入睡觉页面后关闭睡觉打卡弹窗，并点击起床'):
                while self.page.timing().waitAndfind(Timing.sleepingClose,1) == True:
                    self.page.timing().click_timing(Timing.sleepingClose)
                    self.page.timing().click_timing(Timing.sleepingWake)
                    time.sleep(2)
                    self.driver.press_keycode(4)
        with allure.step('判断是否成功起床'):
            assert self.page.more().waitAndfind(More.sleepBtn,1) == True

    @allure.story('起床操作')
    def test_wake(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMy(0.5, 0.9, 0.5, 0.4, 200)
        with allure.step('点击起床，关闭起床打卡弹窗'):
            self.page.more().click_more(More.sleepBtn)
            #点击【起床】按钮
            self.driver.tap([(355, 1866), (456, 1900)], 500)
            # 分享弹窗不能被定位，点击返回
            self.driver.press_keycode(4)
        with allure.step('判断是否成功起床'):
            assert self.page.more().waitAndfind(More.sleepBtn, 1) == True



