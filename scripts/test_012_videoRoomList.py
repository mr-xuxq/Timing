#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base
phone = 10000000100                                         # 登录手机
pwd = 111111                                                # 登录密码
class Test_videoRoom():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    def test_videoRoom(self):
        with allure.step('点击自习室按钮'):
            self.page.shouye().click_videoRoom()
            time.sleep(3)
        with allure.step('检测是否存在自习室，并点击'):
            self.page.video_room_list().check_join()
        with allure.step('断言:成功进入自习室大厅'):
            assert self.page.video_hall().waitAndFind() == True

