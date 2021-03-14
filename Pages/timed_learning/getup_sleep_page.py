#——————起床睡觉——————#
#coding:utf-8
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Getup_sleep(BaseAction):
    # 起床按钮
    getupBtn = By.ID, 'com.huiian.timing:id/popupwindow_getup_ll'
    # 起床-关闭按钮
    wakeBtn = By.ID, 'com.huiian.timing:id/close_iv'
    # 起床-生成卡片
    getupCard = By.ID, 'com.huiian.timing:id/status_dk_img'

    # 睡觉按钮
    sleepBtn = By.ID, 'com.huiian.timing:id/popupwindow_sleep_ll'
    # 睡觉-关闭按钮s
    closeSleepCardBtn = By.ID, 'com.huiian.timing:id/close_iv'
    # 睡觉-生成卡片
    sleepCard = By.ID, 'com.huiian.timing:id/status_dk_img'
    # 睡觉-再起床
    sleepThenGetupBtn = By.ID, 'com.huiian.timing:id/wake_tv'

    def click_getupBtn(self):
        self.click(self.getupBtn)
    def click_wakeBtn(self):
        self.click(self.wakeBtn)
    def click_getupCard(self):
        self.click(self.getupCard)
    def click_sleepBtn(self):
        self.click(self.sleepBtn)
    def click_closeSleepCardBtn(self):
        self.click(self.closeSleepCardBtn)
    def click_sleepCard(self):
        self.click(self.sleepCard)
    def click_sleepAndGetupBtn(self):
        self.click(self.sleepThenGetupBtn)
    def press_back(self):
        self.press_back()
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def check_getupCard(self):
        return self.is_feature_exist(self.getupCard)
    def check_sleepCard(self):
        return self.is_feature_exist(self.sleepCard)