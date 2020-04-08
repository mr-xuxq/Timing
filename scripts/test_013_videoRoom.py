#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base
class Test_videoRoom():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    def test_videoRoom_visitor(self):
        with allure.step('点击自习室按钮'):
            self.page.shouye().click_videoRoom()
            time.sleep(3)
        with allure.step('检测是否存在自习室，并点击'):
            result = self.page.video_room_list().check_join()
            if result == "":
                with allure.step('当前没有开启的自习室，用例结束'):
                    pass
            else:
                self.page.video_room_list().click_joinBtn()
                time.sleep(2)
                with allure.step('点击快速进入按钮'):
                    self.page.video_hall().click_quicklyJoin()
                    time.sleep(2)
                    self.page.video_hall().coordinateClick()
                    time.sleep(5)
                with allure.step('点击退出按钮'):
                    self.page.video_room().click_exit()
                with allure.step('断言:成功退出自习室'):
                    assert self.page.video_hall().waitAndFind() == True
