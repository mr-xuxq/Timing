#coding:utf-8
import time,allure,pytest,os,random
from Api.login import Login
import pandas as pd
from sqlalchemy import create_engine
from appium import webdriver
phone = 10000001000
nickName = 100
password = 111111
# 此处填入服务器连接
engine = create_engine('mysql+pymysql://timing_read_only:db_only_hsyt21@rr-bp12u85w22spt5976do.mysql.rds.aliyuncs.com:3306/timing?charset=utf8')

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'WOSSPVSSUC4S4LUW',
    'platformVersion': '9.0.0',
    'appPackage': 'com.huiian.timing',
    'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
    'newCommandTimeout':'28888'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(8)
class Register():
    def getSize(self):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)
    def tapOperat(self, x, y):
        l = self.getSize()
        X= int(l[0] * x)
        Y= int(l[1] * y)
        driver.tap([(X,Y)],1)
    def swipeOperat(self,x1, y1, x2, y2, t):
        l = self.getSize()
        X1 = int(l[0] * x1)
        X2 = int(l[0] * x2)
        Y1 = int(l[1] * y1)
        Y2 = int(l[1] * y2)
        driver.swipe(X1, Y1, X2, Y2, t)
    def registerAccount(self):
        # 点击更多按钮
        driver.find_element_by_id("com.huiian.timing:id/iv_main_more").click()
        # 点击树洞对讲机、
        time.sleep(2)
        driver.find_element_by_xpath('//*[@text="树洞对讲机"]').click()
        for i in range(1,150):
            # 点击创建房间
            driver.find_element_by_id("com.huiian.timing:id/creation_fm").click()
            # # 点击开麦
            time.sleep(1)
            self.tapOperat(0.16, 0.935)
            # 点击退出
            time.sleep(1)
            self.tapOperat(0.082, 0.068)
            # 确定退出
            driver.find_element_by_id("com.huiian.timing:id/popupwindow_confirm_left_tv").click()
            # 下拉刷新
            time.sleep(2)
            self.swipeOperat(0.5, 0.2, 0.5, 0.8, 500)
        # # 插个话
        # self.swipeOperat(0.319,0.933,0.597,0.933,5000)
        # # 点击发图片
        # time.sleep(2)
        # self.tapOperat(0.751,0.933)
        # # 点击选图片
        # driver.find_element_by_id("com.huiian.timing:id/tv_duration").click()
        # # 点击上墙
        # driver.find_element_by_id("com.huiian.timing:id/tv_up_wall").click()
        # # 点击组个学习局
        # self.tapOperat(0.592, 0.348)
        # # 取消学习据
        # driver.find_element_by_id("com.huiian.timing:id/iv_close").click()
        # # 确定取消
        # driver.find_element_by_id("com.huiian.timing:id/popupwindow_confirm_right_fl").click()
        # # 点击分享
        # driver.find_element_by_id("com.huiian.timing:id/iv_more").click()
        # # 分享到关注我的人
        # driver.find_element_by_id("com.huiian.timing:id/ll_follower").click()
        # # 点击发布
        # driver.find_element_by_id("com.huiian.timing:id/tv_post").click()

        # 继续退出
        driver.find_element_by_id("com.huiian.timing:id/iv_back").click()


if __name__ == '__main__':
    Register().registerAccount()