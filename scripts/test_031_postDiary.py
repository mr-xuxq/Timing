#coding:utf-8
<<<<<<< HEAD
from Pages.page import Page
from base.base_driver import Base
import allure,time
sourse = []

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
=======
import time,allure
from Pages.page import Page
from base.base_driver import Base

class Test_postDiary():
    # setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
    # 放一些准备的工作，或者准备一些测试数据。
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    # tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
    # 当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
>>>>>>> cc7c6a99bd5e5351cc727f0cce76f609c094a754
    def teardown(self):
        self.driver.quit()
    #判断元素是否在当前页面内
    sourse = []
<<<<<<< HEAD
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))
    def test_postDiary(self):
        with allure.step('点击 + 号按钮'):
            self.page.post_content().click_post()
        with allure.step('点击日记按钮'):
            #self.page.post_content().click_postDiary()
            time.sleep(3)
            self.page.post_content().tapOperat(0.752, 0.831)
        with allure.step('输入日记内容'):
            self.page.post_diary().input_diaryContent(12345)
        with allure.step('点击发布'):
            self.page.post_diary().click_post()
        with allure.step('点击确定'):
            self.page.select_cover().click_next()
        with allure.step('断言：发布成功'):
            assert self.page.follow().check_postSuccess() == True

    def test_logout(self):
        with allure.step('检测登陆状态'):
            result = self.page.shouye().check_shouye()
            if result == True:
                with allure.step('点击更多按钮'):
                    self.page.more().click_more()
                    time.sleep(8)
                with allure.step('点击设置按钮'):
                    self.page.more().click_setting()
                with allure.step('点击退出登录按钮'):
                    self.page.setting().click_logout()
                with allure.step('确定退出'):
                    self.page.setting().click_confirmLogout()
                    time.sleep(2)
                with allure.step('断言:退出登录成功'):
                    assert self.page.setting().check_target() == True
            else:
                with allure.step('处于未登录状态，用例结束'):
                    pass
=======
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    #长视频列表页浏览测试用例
    def test_postDiary(self):
        with allure.step('进入更多页'):
            self.page.more().click_more()
        with allure.step('滑动到最底部'):
            time.sleep(3)
            self.page.more().swipeUp()
        with allure.step('点击发布/投稿'):
            self.page.more().click_postBtn()
        with allure.step('点击发布图文日记'):
            self.page.post().click_postDiary()
        with allure.step('输入日记内容'):
            self.page.post_diary().input_diaryContent(12345)
        with allure.step('点击发布按钮'):
            self.page.post_diary().click_post()
        with allure.step('点击确定按钮'):
            time.sleep(2)
            self.page.select_cover().click_next()
            time.sleep(15)
        with allure.step('断言:发布成功'):
            if self.page.follow().check_deleteDiaryBtn() == True:
                self.page.follow().click_deleteDiaryBtn()
                self.page.follow().click_yesBtn()
                return True
            else:
                return False

>>>>>>> cc7c6a99bd5e5351cc727f0cce76f609c094a754
