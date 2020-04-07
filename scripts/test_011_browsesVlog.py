#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base

class Test_browsesVlog():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    # 长视频列表页浏览测试用例
    def test_browsesVlog(self):
        with allure.step('点击sVlog标题'):
            self.page.shouye().click_sVlog()
            time.sleep(2)
        with allure.step('浏览长视频列表'):
            for i in range(1,100):
                self.page.sVlog_list().swipeUp()
        with allure.step('断言:无任何崩溃闪退'):
            assert self.page.sVlog_list().waitAndFind() == True
