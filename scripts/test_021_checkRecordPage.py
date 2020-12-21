#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base

class Test_checkVideoRecordPage():
    # setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
    # 放一些准备的工作，或者准备一些测试数据。
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    # tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
    # 当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
    def teardown(self):
        self.driver.quit()
    #判断元素是否在当前页面内
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    #长视频列表页浏览测试用例
    def test_checkVideoRecordPage(self):
        with allure.step('进入消息页'):
            self.page.shouye().click_message()
            time.sleep(2)
        with allure.step('进入Timing小书童'):
            self.page.message().click_timingService()
        with allure.step('退出Timing小书童'):
            self.page.message().click_back()
        with allure.step('进入道友聊天页'):
            self.page.message().click_firstChannel()
        with allure.step('点击说话就拍按钮'):
            self.page.video_record().click_speakBtn()
        with allure.step('点击开始录制'):
            time.sleep(2)
            self.page.video_record().tapScreen(0.5, 0.84)
        with allure.step('检查界面元素'):
            with allure.step('检查后退按钮'):
                if self.page.video_record().check_back() == True:
                    assert True
                else:
                    assert False
            with allure.step('检查顶部标题'):
                if self.page.video_record().check_titleWord() == True:
                    assert True
                else:
                    assert False
            with allure.step('检查发送对象'):
                if self.page.video_record().check_sendTarget() == True:
                    assert True
                else:
                    assert False
            with allure.step('检查引导文案'):
                if self.page.video_record().check_guideWord() == True:
                    assert True
                else:
                    assert False
            with allure.step('检查美颜按钮'):
                if self.page.video_record().check_switchCamera() == True:
                    assert True
                    with allure.step('点击美颜按钮'):
                        self.page.video_record().click_beautyBtn()
                else:
                    assert False
            with allure.step('检查切换摄像头按钮'):
                if self.page.video_record().check_beautyBtn() == True:
                    assert True
                    with allure.step('点击摄像头按钮'):
                        self.page.video_record().click_switchCamera()
                    with allure.step('连点切换摄像头'):
                        time.sleep(3)
                        self.page.video_record().tapScreen(0.5, 0.5)
                        time.sleep(0.2)
                        self.page.video_record().tapScreen(0.5, 0.5)
                else:
                    assert False
            with allure.step('检查头套按钮'):
                if self.page.video_record().check_hatsBtn() == True:
                    assert True
                    with allure.step('点击头套按钮'):
                        self.page.video_record().click_hatsBtn()
                else:
                    assert False
            with allure.step('检查柠檬头'):
                if self.page.video_record().check_beginToRecord() == True:
                    assert True
                    with allure.step('滑动柠檬头进入说话就拍状态'):
                        self.page.video_record().swipeToSpeak()
                else:
                    assert False
            with allure.step('断言：成功进入录制状态'):
                assert self.page.video_record().check_readyToSpeak() == True


