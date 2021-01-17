#！/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xinlan time:2021/1/17
#个人主页的timingid and 二维码
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class More(BaseAction):
    #更多按钮
    morebuttons = By.ID,'com.huiian.timing:id/mine_img'
    #点击进入个人主页
    personalinfo = By.ID,'com.huiian.timing:id/iv_go'
    #点击id
    timingID = By.ID,'com.huiian.timing:id/tv_timing_id'
    #点击二维码
    QR_code = By.ID,'com.huiian.timing:id/iv_qr_code'



def click_more(self):
    self.click(self.morebuttons)
def click_personalinfo(self):
    self.click(self.personalinfobuttons)
def click_timingID(self):
    self.click(self.timingIDbuttons)