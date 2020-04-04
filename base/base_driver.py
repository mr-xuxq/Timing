#coding:utf-8
from appium import webdriver
from base.base_getDevices import Get

class Base(object):

    def init_driver(self):
        x = Get.result[0]
        y = Get.result[1]

        desired_caps = {
            'platformName': 'Android',
            'deviceName': x,
            'platformVersion': y,
            'appPackage': 'com.huiian.timing',
            'appActivity': '.view.activity.StartupActivity',
            # 应用持续开启时间
            'newCommandTimeout': '28888',
            # 'unicodeKeyboard': True,
            # 'resetKeyboard': True
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver