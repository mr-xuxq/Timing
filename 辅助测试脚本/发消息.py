#coding:utf-8
import time,allure,pytest,os,random
from sqlalchemy import create_engine
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '172.18.0.143:5556',
    'platformVersion': '9.0.0',
    'appPackage': 'com.huiian.timing',
    'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
    'newCommandTimeout':'28888',
    'udid': '172.18.0.143:5556'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(8)
class Sendmessage():
    def getSize(self):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)
    def swipeOperat(self,x1, y1, x2, y2, t):
        l = self.getSize()
        X1 = int(l[0] * x1)
        X2 = int(l[0] * x2)
        Y1 = int(l[1] * y1)
        Y2 = int(l[1] * y2)
        driver.swipe(X1, Y1, X2, Y2, t)

    def sendmessage(self):
        #   点击消息按钮
        driver.find_element_by_id("com.huiian.timing:id/message_img").click()
        #   点击channel
        driver.find_element_by_id("com.huiian.timing:id/cl_content").click()
        #   点击聊天框
        driver.find_element_by_id("com.huiian.timing:id/editTextMessage").click()
        #   点击发送消息
        L = self.getSize()
        for i in range(1,1000):
            driver.tap([(L[0] * 0.83, L[1] * 0.66)], 1)
            time.sleep(0.3)
            driver.tap([(L[0] * 0.83, L[1] * 0.66)], 1)
            time.sleep(0.5)
            driver.tap([(L[0]*0.925,L[1]*0.523)],1)
if __name__ == '__main__':
    Sendmessage().sendmessage()