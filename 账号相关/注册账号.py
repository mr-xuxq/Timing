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
    def swipeOperat(self,x1, y1, x2, y2, t):
        l = self.getSize()
        X1 = int(l[0] * x1)
        X2 = int(l[0] * x2)
        Y1 = int(l[1] * y1)
        Y2 = int(l[1] * y2)
        driver.swipe(X1, Y1, X2, Y2, t)
    def registerAccount(self):
        # 点击手机号登录'
        driver.find_element_by_id("com.huiian.timing:id/ll_lbp").click()
        # 查询尚未注册的手机号并填入
        ID = "1"
        Phone = phone
        while len(ID) == 1:
            Phone = Phone + random.randint(10000, 99999)
            file = open('../account.txt', 'a')  # 开启文件准备记录
            file.write(str(Phone) + '\n')
            file.flush()
            file.close()
            ID = pd.read_sql('SELECT ID FROM t_user where phone="' + str(Phone) + '" ', engine)
        # 输入手机号'):
        driver.find_element_by_id("com.huiian.timing:id/phone_et").send_keys(Phone)
        # 点击获取验证码按钮'):
        driver.find_element_by_id("com.huiian.timing:id/login_verify_tv").click()
        time.sleep(2)
        # 从数据库拿验证码
        captcha = pd.read_sql('select captcha FROM t_captcha WHERE phone = "' + str(Phone) + '" order by postTime desc',engine)
        captcha = captcha.iloc[0, 0]
        # 输入验证码
        driver.find_element_by_id("com.huiian.timing:id/captcha_et").send_keys(captcha)
        # 点击完成，进入学习标签页
        driver.find_element_by_id("com.huiian.timing:id/login_verify_tv").click()
        # 点击选择标签
        time.sleep(2)
        self.swipeOperat(0.5,0.9,0.5,0.4,500)
        time.sleep(1)
        driver.find_element_by_id("com.huiian.timing:id/tv_name").click()
        # driver.find_element_by_xpath('//*[@text="英语"]').click()
        # 点击下一步
        driver.find_element_by_id("com.huiian.timing:id/tv_next").click()
        # 点击选择头像按钮
        driver.find_element_by_id("com.huiian.timing:id/iv_avatar").click()
        # 点击图片，进入图片详情页
        driver.find_element_by_id("com.huiian.timing:id/photo_list_item_img").click()
        # 点击选取按钮，完成图片选择
        driver.find_element_by_id("com.huiian.timing:id/tv_crop_select").click()
        # 输入昵称
        driver.find_element_by_id("com.huiian.timing:id/et_name").send_keys(9527)
        # 选择男性
        driver.find_element_by_id("com.huiian.timing:id/tv_male").click()
        # 设置生日
        driver.find_element_by_id("com.huiian.timing:id/tv_birth").click()
        for i in range(1, 10):
            self.swipeOperat(0.35, 0.93, 0.35, 0.78, 500)
            self.swipeOperat(0.78, 0.93, 0.78, 0.78, 500)
        driver.find_element_by_id("com.huiian.timing:id/tv_ok").click()
        # 点击生成按钮
        driver.find_element_by_id("com.huiian.timing:id/tv_commit").click()
        time.sleep(10)
        # 新手引导-下一步
        driver.find_element_by_id("com.huiian.timing:id/guide_next_page_tv").click()
        # 新手引导-了解组团学习
        time.sleep(6)
        driver.find_element_by_id("com.huiian.timing:id/change_found_firend_tv").click()
        # 新手引导-暂不需要按钮
        time.sleep(3)
        driver.find_element_by_id("com.huiian.timing:id/guide_next_module_tv").click()
        time.sleep(2)
        # 新手引导-开启Timing之旅
        driver.find_element_by_id("com.huiian.timing:id/guide_next_page_tv").click()
        # 设置密码
        Login().reset_password(Phone,captcha,password)

        time.sleep(5)
        # 准备退出，点击更多按钮
        driver.find_element_by_id("com.huiian.timing:id/mine_img").click()
        time.sleep(4)
        # 点击设置按钮
        driver.find_element_by_id("com.huiian.timing:id/iv_setting").click()
        # 点击退出登录按钮
        driver.find_element_by_id("com.huiian.timing:id/logout_tv").click()
        # 确定退出
        driver.find_element_by_id("com.huiian.timing:id/popupwindow_confirm_right_tv").click()



if __name__ == '__main__':
    for k in range(1,40):
        Register().registerAccount()