import time, allure
from base.base_driver import Base
from Pages.page import Page
from appium.webdriver.common.touch_action import TouchAction

#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
@allure.feature('计时功能')
class Test_normalTiming():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
        self.action = TouchAction(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('学习计时达1min操作')
    def test_normalTiming(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(2)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMore()
            time.sleep(3)
        with allure.step('点击学习计时按钮，设定内容后开始'):
            self.page.more().click_normalTiming()
            self.page.timing().input_studyContentBox('This is Timing')
            self.page.timing().click_studySettingBtn()
            #概率性的选取失败
            e1 = self.driver.find_element_by_xpath("//*[@text='01']")
            self.action.long_press(e1, None, None, 400).perform()
            self.page.timing().click_studySettingsuccessBtn()
            self.page.timing().click_startTimingBtn()
            time.sleep(62)
        with allure.step('校验结果：计时1min后关闭计时的后续操作执行后判断计时是否正常结束'):
            if self.page.timing().check_timingDialog() == True:
                self.page.timing().click_timingDialog()
                self.page.timing().click_timingEnd()
            else:
                self.page.timing().click_timingEnd()
                if self.page.timing().check_timingEndDialog() == True:
                    self.page.timing().click_timingEndDialog()
                else:
                    assert self.page.timing().waitAndfind_timingEndSuccess() == True

    @allure.story('学习计不足1min操作')
    def test_normalTiming_exit(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(5)
        with allure.step('滑动更多页面至底部'):
            self.page.more().swipeByMore()
            time.sleep(2)
        with allure.step('点击学习计时按钮，设定内容后开始'):
            self.page.more().click_normalTiming()
            self.page.timing().input_studyContentBox('This is Timing')
            self.page.timing().click_studySettingBtn()
            time.sleep(5)
            #滑动选择1min
            e1 = self.driver.find_element_by_xpath("//*[@text='01']")
            #概率性的选取失败
            self.action.long_press(e1, None, None, 400).perform()
            self.page.timing().click_studySettingsuccessBtn()
            self.page.timing().click_startTimingBtn()
            time.sleep(5)
        with allure.step('计时不足1min后关闭计时'):
            self.page.timing().click_timingEnd()
            self.page.timing().click_timingEndConfirmRight()
        with allure.step('校验结果：计时不足1min后关闭计时的判断该段计时是否没有记录'):
            #点击【结束】后，是否快速返回至更多页面
            assert self.page.more().waitAndfind_more() == True
