#coding:utf-8
import time,allure,pytest,os,random
import pandas as pd
from sqlalchemy import create_engine
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'WOSSPVSSUC4S4LUW',
    'platformVersion': '9.0.0',
    'appPackage': 'com.huiian.timing',
    'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
    'newCommandTimeout':'28888'
    'automationName":"UiAutomator2'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(15)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
l = getSize()
def swipeOperat(x1, y1, x2, y2, t):
    X1 = int(l[0] * x1)
    X2 = int(l[0] * x2)
    Y1 = int(l[1] * y1)
    Y2 = int(l[1] * y2)
    driver.swipe(X1, Y1, X2, Y2, t)
def clickOperat(x,y):
    driver.tap([(x*l[0],y*l[1])],1)

# 操作前请手动进入录制页:
# 反复点击切换摄像头
clickOperat(0.5, 0.966)
time.sleep(2)
clickOperat(0.124, 0.66)
time.sleep(2)
clickOperat(0.497, 0.853)
time.sleep(2)
for j in range(1,10):
    for i in  range(1,1000):
        clickOperat(0.792, 0.817)
        time.sleep(0.2)
        clickOperat(0.904,0.147)
        time.sleep(0.2)
        clickOperat(0.251, 0.9)
        time.sleep(0.5)
        clickOperat(0.904,0.212)
        time.sleep(0.2)
        swipeOperat(0.143, 0.824, 0.585, 0.818, 800)
        time.sleep(0.2)
        clickOperat(0.792, 0.817)
        time.sleep(0.2)
        clickOperat(0.748, 0.903)
        time.sleep(0.5)
        clickOperat(0.904,0.212)
        time.sleep(0.2)
        swipeOperat(0.143, 0.824, 0.585, 0.818, 800)
        time.sleep(0.2)
        clickOperat(0.792, 0.817)
        time.sleep(0.2)
        clickOperat(0.1, 0.99)
        time.sleep(0.5)
        clickOperat(0.251, 0.9)
        time.sleep(0.5)
    # # 滑动准备好了
    # swipeOperat(0.143, 0.824,0.585, 0.818,800)
    # if j%2 == 0:
    #     clickOperat(0.151, 0.688)
    #     time.sleep(2)
    #     clickOperat(0.085, 0.964)
    #     time.sleep(2)
    # else:
    #     pass
