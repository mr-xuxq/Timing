import time,allure
from Pages.page import Page
from base.base_driver import Base

@allure.feature('刷首页算法')
class Test_browseShowye():
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()

    def test_browseShowye(self):
        time.sleep(5)
        with allure.step('检测登陆状态'):
            result = self.page.shouye().check_shouye()
            if result == True:
                with allure.step('登陆到首页成功，开始浏览'):
                    i = 0
                    while i<50:
                        self.page.shouye().swipeByShouye()
                        i += 1
                    with allure.step('断言：浏览无闪退'):
                        assert self.page.shouye().check_shouye() == True
            else:
                with allure.step('登陆到首页超时或失败，结束用例'):
                    pass