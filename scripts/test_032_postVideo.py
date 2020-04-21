#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base

class Test_postDiary():
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
    def test_postVideo(self):
        time.sleep(5)
        with allure.step('进入发布页'):
            self.page.shouye().click_post()
        with allure.step('点击发布长视频'):
            self.page.post_content().click_postVideo()
        with allure.step('选择第一个视频'):
            self.page.select_diary_video().click_selectVideoBtn()
        with allure.step('点击下一步按钮'):
            self.page.select_diary_video().click_nextBtn()
            time.sleep(1)
        with allure.step('继续点击下一步按钮'):
            self.page.select_diary_video().click_nextBtn()
        with allure.step('添加标题'):
            self.page.post_video().input_addTitleBox("this is my svlog")
        with allure.step('点击发布'):
            self.page.post_video().click_post()
            time.sleep(60)
        with allure.step('断言:长视频发布成功'):
            assert self.page.follow().check_deleteDiaryBtn() == True

    def test_deleteVideo(self):
        time.sleep(5)
        with allure.step('检测登陆状态'):
            result = self.page.shouye().check_shouye()
            if result == True:
                self.page.follow().click_follow()
                self.page.follow().click_deleteDiaryBtn()
                self.page.follow().click_yesBtn()
                time.sleep(3)
                result = self.page.follow().check_deleteDiaryBtn()
                with allure.step('断言:删除视频日记成功'):
                    assert result == False
            else:
                with allure.step('登陆到首页超时或失败，结束用例'):
                    pass
