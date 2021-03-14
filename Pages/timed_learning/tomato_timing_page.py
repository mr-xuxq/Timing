#coding:utf-8
#——————番茄计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Tomato_timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 计时页面确定结束按钮
    timingEndYes = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_tv'
    # 番茄计时_取消按钮
    timingTomatoCancel = By.ID, 'com.huiian.timing:id/tomato_cancel_tv'

    def click_timingDialog(self):
        self.click(self.timingDialog)
    def press_back(self):
        self.press_back()
    def click_timingTomatoCancel(self):
        self.click(self.timingTomatoCancel)
    def click_timingEndYes(self):
        self.click(self.timingEndYes)
    def check_timingDialog(self):
        return self.is_feature_exist(self.timingDialog)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)