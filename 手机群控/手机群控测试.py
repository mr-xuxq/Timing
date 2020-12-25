# coding=utf-8
from appium import webdriver
import time
import threading
desired_caps1 = {
                'platformName': 'Android',
                'deviceName': '192.168.88.177:5555',
                'platformVersion': '5.1.1',
                # apk包名
                'appPackage': 'com.huiian.timing',
                # apk的launcherActivity
                'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
                'udid': '192.168.88.177:5555'
                }
desired_caps2 = {
                'platformName': 'Android',
                'deviceName': '192.168.88.69:5556',
                'platformVersion': '8.1.0',
                # apk包名
                'appPackage': 'com.huiian.timing',
                # apk的launcherActivity
                'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
                'udid': '192.168.88.69:5556'
                }
desired_caps3 = {
                'platformName': 'Android',
                'deviceName': '192.168.88.136:5557',
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.huiian.timing',
                # apk的launcherActivity
                'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
                'udid': '192.168.88.136:5557'
                }

def task1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
    ##休眠20s等待页面加载完成
    time.sleep(20)
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

    def clickOperat(x, y):
        driver.tap([(x * l[0], y * l[1])], 1)

    # 操作前请手动进入录制页:
    # 反复点击切换摄像头
    for j in range(1, 10):
        print(j)
        for i in range(1, 100):
            clickOperat(0.904, 0.147)
            time.sleep(0.2)
        # 反复点击美颜按钮
        for i in range(1, 50):
            clickOperat(0.904, 0.212)
            time.sleep(0.2)
        # 反复点击头套按钮
        for i in range(1, 200):
            clickOperat(0.792, 0.817)
            time.sleep(0.2)
        # 滑动准备好了
        swipeOperat(0.143, 0.824, 0.585, 0.818, 800)
        if j % 2 == 0:
            clickOperat(0.151, 0.688)
            time.sleep(2)
            clickOperat(0.085, 0.964)
            time.sleep(2)
        else:
            pass
    driver.quit()

def task2():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    ##休眠20s等待页面加载完成
    time.sleep(20)
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

    def clickOperat(x, y):
        driver.tap([(x * l[0], y * l[1])], 1)

    # 操作前请手动进入录制页:
    # 反复点击切换摄像头
    for j in range(1, 10):
        print(j)
        for i in range(1, 100):
            clickOperat(0.904, 0.147)
            time.sleep(0.2)
        # 反复点击美颜按钮
        for i in range(1, 50):
            clickOperat(0.904, 0.212)
            time.sleep(0.2)
        # 反复点击头套按钮
        for i in range(1, 200):
            clickOperat(0.792, 0.817)
            time.sleep(0.2)
        # 滑动准备好了
        swipeOperat(0.143, 0.824, 0.585, 0.818, 800)
        if j % 2 == 0:
            clickOperat(0.151, 0.688)
            time.sleep(2)
            clickOperat(0.085, 0.964)
            time.sleep(2)
        else:
            pass
    driver.quit()

def task3():
    driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub', desired_caps3)
    ##休眠20s等待页面加载完成
    time.sleep(40)
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

    def clickOperat(x, y):
        driver.tap([(x * l[0], y * l[1])], 1)

    # 操作前请手动进入录制页:
    # 反复点击切换摄像头
    for j in range(1, 10):
        print(j)
        for i in range(1, 100):
            clickOperat(0.904, 0.160)
            time.sleep(0.2)
        # 反复点击美颜按钮
        for i in range(1, 50):
            clickOperat(0.904, 0.232)
            time.sleep(0.2)
        # 反复点击头套按钮
        for i in range(1, 200):
            clickOperat(0.792, 0.817)
            time.sleep(0.2)
        # 滑动准备好了
        swipeOperat(0.143, 0.824, 0.585, 0.818, 1000)
        if j % 2 == 0:
            clickOperat(0.151, 0.688)
            time.sleep(2)
            clickOperat(0.085, 0.964)
            time.sleep(2)
        else:
            pass
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