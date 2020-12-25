from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import datetime
import random
import time
# 主要按钮纳入数组，创建群 & 破茧训练营 目前不做处理
functionaPoint = ["学习计时","视频打卡","学习农场","番茄计时","自习室","图书馆","起床睡觉","学习计划","创建群","破茧训练营"]
today = datetime.date.today()
desired_caps = {
    'platformName': 'Android',
    'deviceName': '559bee8c',
    'platformVersion': '5.1.1',
    'appPackage': 'com.huiian.timing',
    'appActivity': 'com.huiian.timing.view.activity.StartupActivity',
    'newCommandTimeout':'28888'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
action = TouchAction(driver)
# 获取
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
l = getSize()
def swipe(swipeLeft,swipeHeight):
    x1 = int(l[0] * 0.5)
    x2 = int(l[0] * swipeLeft)
    y1 = int(l[1] * 0.5)
    y2 = int(l[1] * (swipeHeight))
    driver.swipe(x1, y1, x2, y2, 800)
def startFunction(i):
    # 进入A5我页面
    driver.find_element_by_id("com.huiian.timing:id/tab_mine_ll").click()
    time.sleep(2)
    swipe(0.5,0.01)
    time.sleep(2)
    # 打开对应功能
    driver.find_element_by_xpath("//*[@text = '" + str(functionaPoint[i]) + "']").click()
    # 计时判定
    if i < 4:
        # 预设类型计时
        driver.find_element_by_id("com.huiian.timing:id/et_title").send_keys(111111)
        if i< 3:
            try:
                driver.find_element_by_id("com.huiian.timing:id/tv_setting_time").click()       # 点击时长设定
            except Exception as e:
                time.sleep(1)
                driver.tap([(l[0] * 0.9 , l[1] * 0.45)],1)
                time.sleep(1)
            else:
                pass
            e1 = driver.find_element_by_xpath("//*[@text='01']")                            # 设定时长1分钟
            action.long_press(e1, None, None, 800).perform()
            # action.long_press(e1, None, None, 800).perform()
            driver.find_element_by_id("com.huiian.timing:id/common_confirm_tv").click()     # 点击完成时间设定
            time.sleep(1)
        driver.find_element_by_id("com.huiian.timing:id/tv_confirm").click()                #点击开始学习

        if i == 1:
            driver.find_element_by_id("com.huiian.timing:id/tv_start_recording").click()    # 点击视频的开始学习按钮
            time.sleep(5)
        print("   ")
        print("开始"+ functionaPoint[i] + "成功")
        time.sleep(8)
def endTime(i,iscomplete):
    time.sleep(3)
    if   i==1:
        driver.find_element_by_id("com.huiian.timing:id/htv_end").click()                   # 结束视频学习
    elif i==2:
        driver.find_element_by_id("com.huiian.timing:id/end_tv").click()                        # 结束农场学习
    elif i==3:
        if iscomplete == 0:
            driver.find_element_by_id("com.huiian.timing:id/tomato_cancel_tv").click()      # 结束番茄学习
        else:
            driver.find_element_by_id("com.huiian.timing:id/tomato_done_tv").click()        # 完成番茄学习
    else:
        driver.find_element_by_id("com.huiian.timing:id/timing_stop_tv").click()            # 结束自由学习
    try:
        driver.find_element_by_id("com.huiian.timing:id/popupwindow_confirm_right_tv").click()  # 点击确定
    except Exception as e:
        pass
    if iscomplete == 0:
        print("结束" + functionaPoint[i] + "成功")
    else:
        print("完成" + functionaPoint[i] + "成功")
    time.sleep(8)
def functionProcess(i,iscomplete):                                                      # iscomplete若为 0 则表示非正常计时，为 1 表示正常完成计时
    if  iscomplete == 0:
        endTime(i,iscomplete)
    elif iscomplete == 1:
        if i ==3:
            time.sleep(1510)
            driver.find_element_by_id("com.huiian.timing:id/popupwindow_tip_got_tv").click()  # 点击我知道了
            endTime(i,iscomplete)
        else:
            time.sleep(62)
            driver.find_element_by_id("com.huiian.timing:id/popupwindow_tip_got_tv").click()            # 点击我知道了
            if  i == 0:
                k = random.randint(0,1)
                if k == 0:
                    driver.find_element_by_id("com.huiian.timing:id/tv_timing_again").click()           # 点击再学30min
                    time.sleep(2)
                    endTime(i,iscomplete)
                else:
                    driver.find_element_by_id("com.huiian.timing:id/tv_timing_times_up_end").click()    # 点击结束按钮
                    print("完成" + functionaPoint[i] + "成功")
            elif i == 1:
                endTime(i,iscomplete)
                time.sleep(10)
            elif i == 2:
                endTime(i,iscomplete)
        time.sleep(8)
        try:
            driver.find_element_by_id("com.huiian.timing:id/tv_know").click()  # 点击知道了按钮
        except Exception as e:
            pass
        try:
            driver.find_element_by_id("com.huiian.timing:id/iv_close").click()                         # 点击 X 按钮
        except Exception as e:
            pass
        time.sleep(8)
        try:
            driver.find_element_by_id("com.huiian.timing:id/tv_finish").click()                         # 点击完成按钮
        except Exception as e:
            driver.find_element_by_xpath("//*[@text = '完成']").click()
        if i == 1:
            try:
                driver.find_element_by_id("com.huiian.timing:id/iv_close").click()                      # 点击左上角关闭按钮
            except Exception as e:
                pass
    if i == 4:
            pass
for k in range(0,2):
    for i in range(0,4):
        for j in range(0,2):
            startFunction(i)
            functionProcess(i,iscomplete=j)
