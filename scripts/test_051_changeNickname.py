#coding:utf-8
import time,allure,random
from Pages.page import Page
from base.base_driver import Base
#from base.base_analyze import analyze_file
import pandas as pd
from sqlalchemy import create_engine
#phone = 10000000000 + random.randint(1, 99)
phone = 10000000001
#此处填入数据库连接
engine1 = create_engine('mysql+pymysql://timing_read_only:db_only_hsyt21@rr-bp12u85w22spt5976do.mysql.rds.aliyuncs.com:3306/timing?charset=utf8')


class Test_changeNickname():
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
    def test_changeNickname(self):
        with allure.step('点击更多按钮'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('进入个人主页'):
            self.page.more().click_person()
            time.sleep(1)
        with allure.step('点击修改资料'):
            self.page.person_home().click_personInfo()
            time.sleep(5)
        with allure.step('点击修改姓名'):
            self.page.edit_personal_info().tapScreen(0.5,0.377)
            time.sleep(1)
        with allure.step('修改姓名'):
            name = random.randint(1, 200000)
            self.page.name_info().input_nameBox(name)
            time.sleep(1)
        with allure.step('点击确定'):
            self.page.name_info().click_nameRight()
            time.sleep(1)
        with allure.step('断言：修改请求完成'):
            self.page.edit_personal_info().check_backBtn()


