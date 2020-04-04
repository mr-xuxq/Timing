import time, allure
from Pages.timing_page import Timing
from Pages.more_page import More
from Pages.page import Page
from base.base_driver import Base
#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
@allure.feature('计时功能')
class Test_normalTiming():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('学习计时操作')
    def test_normalTiming(self):
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
