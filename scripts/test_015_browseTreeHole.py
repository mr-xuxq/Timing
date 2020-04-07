#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base
phone = 10000000100                                         # 登录手机
pwd = 111111                                                # 登录密码
class Test_treeHole():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    def test_treeHole(self):
        with allure.step('点击树洞对讲机按钮'):
            self.page.tree_hole().click_treeHole()
            time.sleep(3)
            self.page.tree_hole().tapScreen(0.39 , 0.96)
            time.sleep(1)
            self.page.tree_hole().tapScreen(0.39 , 0.96)
        with allure.step('点击树洞对讲机按钮'):
            self.page.tree_hole().click_matchHole()
            for i in range(1,5):
                time.sleep(5)
                self.page.tree_hole().tapScreen(0.73 , 0.87)
        with allure.step('断言:树洞切换频道正常'):
            assert self.page.tree_hole().findChannel() == True