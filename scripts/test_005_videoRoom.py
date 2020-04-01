#coding:utf-8
import time
from Pages.page import Page
from base.base_driver import Base
phone = 10000000100                                         # 登录手机
pwd = 111111                                                # 登录密码
class Test_videoRoom():
    #setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
    #放一些准备的工作，或者准备一些测试数据。
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    #tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
    #当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
    def teardown(self):
        self.driver.quit()
    #判断元素是否在当前页面内
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    #长视频列表页浏览测试用例
    def test_videoRoom(self):
        self.page.shouye().click_videoRoom()                                                                            # 点击Timing自习室
        time.sleep(3)
        self.page.videoRoom_list().check_join()                                                                         # 检测是否存在自习室，并点击
        #断言
        assert self.page.videoHall().waitAndFind() == True

    def test_logout(self):
        self.page.setting().click_more()                                                                                # 点击更多
        self.page.setting().click_setting()                                                                             # 点击设置
        self.page.setting().click_logout()                                                                              # 点击退出登录
        self.page.setting().click_confirmLogout()                                                                       # 点击确定
        assert self.page.setting().findLogin() == True                                                                  # 断言