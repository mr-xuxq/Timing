import time,pytest,allure
from Pages.page import Page
from base.base_driver import Base
from Pages.page import Shouye

@allure.feature('刷首页算法')
class Test_browseShowye():
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()

    def test_swipeO(self):
        time.sleep(5)
        i = 0
        while i<50:
        #while True:
            self.page.shouye().swipeUp()
            i += 1
        #断言
        assert self.page.shouye().waitAndfind(Shouye.shouyeBtn) == True