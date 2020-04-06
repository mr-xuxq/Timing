import time, allure
from Pages.personal_information.more_page import More
from Pages.page import Page
from base.base_driver import Base
#如果你想重复执行测试模块(.py文件)，直接在模块上方（导入pytest包下面）加入下面一行代码即可：pytestmark变量名是固定的~
#pytestmark=pytest.mark.repeat(2)
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