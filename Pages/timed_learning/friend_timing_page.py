#coding:utf-8
#——————学习计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import time

class Firend_timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 学习内容输入框
    friendTimeBox = By.ID, 'com.huiian.timing:id/et_title'
    # 创建按钮
    beginTimeBtn = By.ID, 'com.huiian.timing:id/create_room_btn'
    # 结束学习按钮
    endTimeBtn = By.ID, 'com.huiian.timing:id/tv_study'
    # 结束学习确定按钮
    endTimeYesBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'
    # 去打卡按钮
    gotoDaka = By.ID, 'com.huiian.timing:id/tv_goto_daka'
    # 计时总结栏
    finshTime = By.ID, 'com.huiian.timing:id/total_duration_tv'
    # 创建房间按钮
    creatRoom = By.ID, 'com.huiian.timing:id/createRoom'

    def click_beginTimeBtn(self):
        self.click(self.beginTimeBtn)
    def click_endTimeBtn(self):
        self.click(self.endTimeBtn)
    def click_endTimeYesBtn(self):
        self.click(self.endTimeYesBtn)
    def click_gotoDaka(self):
        self.click(self.gotoDaka)
    def click_creatRoom(self):
        self.click(self.creatRoom)
    def press_back(self):
        self.press_back()

    def input_friendTimeBox(self,content):
        self.input(self.friendTimeBox,content)

    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def check_gotoDaka(self):
        return self.is_feature_exist(self.gotoDaka)
    def check_finshTime(self):
        return self.is_feature_exist(self.finshTime)