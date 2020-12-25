# coding=utf-8
from appium import webdriver
import time
import threading
desired_caps1 = {
                'platformName': 'Android',
                'deviceName': '192.168.88.103:5555',
                'platformVersion': '5.1.1',
                # apk包名
                'appPackage': 'com.huiian.timing',
                # apk的launcherActivity
                'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
                'udid': '192.168.88.103:5555'
                }
desired_caps2 = {
                'platformName': 'Android',
                'deviceName': '192.168.88.217:5556',
                'platformVersion': '8.1.0',
                # apk包名
                'appPackage': 'com.huiian.timing',
                # apk的launcherActivity
                'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
                'udid': '192.168.88.217:5556'
                }
desired_caps3 = {
                'platformName': 'Android',
                'deviceName': '192.168.88.84:5558',
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.huiian.timing',
                # apk的launcherActivity
                'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
                'udid': '192.168.88.84:5558'
                }

def task1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
    ##休眠20s等待页面加载完成
    time.sleep(20)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    for i in range(1,1000):
        for j in range(0,4):
            driver.tap([((0.12 + j * 0.25 ) * x , 0.94 * y )],1)
    print(driver.contexts)
    driver.quit()

def task2():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    ##休眠20s等待页面加载完成
    time.sleep(20)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    for i in range(1,1000):
        for j in range(0,4):
            driver.tap([((0.12 + j * 0.25 ) * x , 0.94 * y )],1)
    print(driver.contexts)
    driver.quit()

def task3():
    driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub', desired_caps3)
    ##休眠20s等待页面加载完成
    time.sleep(20)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    for i in range(1,1000):
        for j in range(0,4):
            time.sleep(0.1)
            driver.tap([((0.12 + j * 0.25 ) * x , 0.94 * y )],1)
    print(driver.contexts)
    driver.quit()

threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)

t2 = threading.Thread(target=task2)
threads.append(t2)

t3 = threading.Thread(target=task3)
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        time.sleep(2)
        t.start()