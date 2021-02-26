#coding:utf-8
#——————学习计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import time

class Farm_timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 学习农场结束按钮
    farmTimeEndBtn = By.ID, 'com.huiian.timing:id/end_tv'
    #计时不足1min点击结束出现的弹窗_【确定】按钮
    timingEndConfirmRight = By.XPATH, '//*[@text="确定"]'
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 学习结束后【去打卡】按钮
    timingEndSuccess = By.ID, 'com.huiian.timing:id/tv_goto_daka'
    # 学习结束后的展示数据卡片
    learningDataCard = By.ID, 'com.huiian.timing:id/timing_info_ll'

    def click_farmTimeEndBtn(self):
        self.click(self.farmTimeEndBtn)
    def click_timingEndConfirmRight(self):
        self.click(self.timingEndConfirmRight)
    def click_timingDialog(self):
        self.click(self.timingDialog)

    def check_timingEndSuccess(self):
        return self.is_feature_exist(self.timingEndSuccess)

    def press_back(self):
        self.press_back()
    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)