#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base
#from base.base_analyze import analyze_file
import pandas as pd
from sqlalchemy import create_engine
phone = 10000000860
nickName = 9527
# 此处填入服务器连接



class Test_registerAccount():
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
    #手机号密码登录测试用例
    def test_registerAccount(self):
        with allure.step('点击手机号登录'):
            self.page.login().click_phone_login()
        with allure.step('查询尚未注册的手机号并填入'):
            ID = "1"
            Phone = phone
            while len(ID) == 1:
                Phone = Phone + 1
                ID = pd.read_sql('SELECT ID FROM t_user where phone="' + str(Phone) + '" ', engine)
            self.page.login_phone().input_phone(str(Phone))
        with allure.step('点击获取验证码按钮'):
            self.page.login_phone().click_getCaptcha()
            time.sleep(2)
        with allure.step('从数据库拿验证码'):
            captcha = pd.read_sql('select captcha FROM t_captcha WHERE phone = "' + str(Phone) + '" order by postTime desc',engine)
            captcha = captcha.iloc[0, 0]
        with allure.step('输入验证码'):
            self.page.login_phone_captcha().input_captcha(str(captcha))
        with allure.step('点击完成，进入学习标签页'):
            self.page.login_phone_captcha().click_loginBtn()
        with allure.step('点击选择标签'):
            time.sleep(2)
            self.page.register_add_tags().click_labelBtn()
        with allure.step('点击下一步'):
            self.page.register_add_tags().click_nextBtn()
        with allure.step('点击选择头像按钮'):
            self.page.register_fillInformation().click_selectPhotoBtn()
        with allure.step('点击图片，进入图片详情页'):
            self.page.select_photo().click_photoBtn()
        with allure.step('点击选取按钮，完成图片选择'):
            self.page.select_photo().click_selectBtn()
        with allure.step('输入昵称'):
            self.page.register_fillInformation().input_nickNameBox(str(nickName))
        with allure.step('选择男性'):
            self.page.register_fillInformation().click_genderBtn()
        with allure.step('设置生日'):
            self.page.register_fillInformation().set_brithday()
        with allure.step('点击生成按钮'):
            self.page.register_fillInformation().click_generateBtn()
            time.sleep(5)
        with allure.step('新手引导-下一步'):
            self.page.guide().click_yesBtn()
        with allure.step('新手引导-了解组团学习'):
            self.page.guide().click_groupTolearnBtn()
        with allure.step('新手引导-暂不需要按钮'):
            self.page.guide().click_noBtn()
            time.sleep(1)
        with allure.step('新手引导-开启Timing之旅'):
            self.page.guide().click_yesBtn()
        with allure.step('断言:注册完成'):
            assert self.page.login().check_target() == True

    def test_logout(self):
        with allure.step('点击更多按钮'):
            self.page.more().click_more()
        with allure.step('点击设置按钮'):
            self.page.more().click_setting()
        with allure.step('点击退出登录按钮'):
            self.page.setting().click_logout()
        with allure.step('确定退出'):
            self.page.setting().click_confirmLogout()
        with allure.step('断言:退出登录成功'):
            assert self.page.setting().findLogin() == True
