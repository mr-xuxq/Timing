#coding:utf-8
import time
from Pages.page import Page
from base.base_driver import Base
#from base.base_analyze import analyze_file
import pandas as pd
from sqlalchemy import create_engine
phone = 10000000773
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
        self.page.login().click_phone_login()                                                                           # 点击手机号登录
        ID = "1"
        Phone = phone
        while len(ID) == 1:
            Phone = Phone + 1
            ID = pd.read_sql('SELECT ID FROM t_user where phone="' + str(Phone) + '" ', engine)
        self.page.login_phone().input_phone(str(Phone))                                                                 # 输入手机号
        #self.page.login_phone().back()                                                                                 # 关小键盘
        self.page.login_phone().click_getCaptcha()                                                                      # 点击获取验证码按钮
        time.sleep(2)
        captcha = pd.read_sql('select captcha FROM t_captcha WHERE phone = "' + str(Phone) + '" order by postTime desc',engine)
        captcha = captcha.iloc[0, 0]  # 正式服数据库拿验证码
        self.page.login_phone_captcha().input_captcha(str(captcha))                                                     # 输入验证码
        self.page.login_phone_captcha().click_loginBtn()                                                                # 点击完成，进入学习标签页
        self.page.register_add_tags().click_labelBtn()                                                                  # 点击选择标签
        self.page.register_add_tags().click_nextBtn()                                                                   # 点击下一步
        self.page.register_fillInformation().click_selectPhotoBtn()                                                     # 点击选择头像按钮
        self.page.selectPhoto().click_photoBtn()                                                                        # 点击图片，进入图片详情页
        self.page.selectPhoto().click_selectBtn()                                                                       # 点击选取按钮，完成图片选择
        self.page.register_fillInformation().input_nickNameBox(str(nickName))                                           # 输入昵称
        self.page.register_fillInformation().click_genderBtn()                                                          # 选择男性
        self.page.register_fillInformation().set_brithday()                                                             # 设置生日
        self.page.register_fillInformation().click_generateBtn()                                                        # 生成按钮
        time.sleep(5)
        self.page.guide().click_yesBtn()                                                                                # 下一步
        self.page.guide().click_groupTolearnBtn()                                                                       # 再了解组团学习按钮
        self.page.guide().click_noBtn()                                                                                 # 暂不需要按钮
        time.sleep(1)
        self.page.guide().click_yesBtn()                                                                                # 开启Timing之旅

        # for i in range(1,5):
        #     time.sleep(1)
        #     self.page.guide().click_yesBtn()                                                                            # 下一步/开启Timing之旅
        #断言
        assert self.page.register_fillInformation().waitAndFind() == True

    def test_logout(self):
        self.page.setting().click_more()
        self.page.setting().click_setting()
        self.page.setting().click_logout()
        self.page.setting().click_confirmLogout()
        assert self.page.setting().findLogin() == True


