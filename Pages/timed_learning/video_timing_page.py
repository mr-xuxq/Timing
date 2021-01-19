#coding:utf-8
#——————学习计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Video_timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 计时页面确定结束按钮
    timingEndYes = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_tv'
    # 计时结算页弹窗【知道了】
    timingEndDialog = By.XPATH, '//*[@text="知道了"]'
    # 第一次点击视频打开，出现视频录制权限弹窗
    videoStartDialog = By.XPATH, '//*[@text="允许"]'
    # 视频打卡结束后_分享视频打卡按钮
    videoSuccess = By.ID, 'com.huiian.timing:id/tv_share'
    #! 视频打卡页面结束_确定按钮
    videoEndDialog = By.XPATH, '//*[@text="确定"]'
    # 视频打卡开始学习按钮
    videoStartStudyBtn = By.ID, 'com.huiian.timing:id/tv_start_recording'
    # 视频打卡页面关闭按钮
    videoCloseBtn = By.ID, 'com.huiian.timing:id/htv_end'

    def click_timingDialog(self):
        self.click(self.timingDialog)
    def click_timingEndYes(self):
        self.click(self.timingEndYes)
    def click_timingEndDialog(self):
        self.click(self.timingEndDialog)
    def click_videoStartDialog(self):
        self.click(self.videoStartDialog)
    def click_videoSuccess(self):
        self.click(self.videoSuccess)
    def click_videoEndDialog(self):
        self.click(self.videoEndDialog)
    def press_back(self):
        self.press_back()

    def click_videoStartStudy(self):
        self.click(self.videoStartStudyBtn)
    def click_videoClosBtn(self):
        self.click(self.videoCloseBtn)

    def check_videoSuccess(self):
        return self.is_feature_exist(self.videoSuccess)

    def check_timingDialog(self):
        if self.find_element(self.timingDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_timingEndDialog(self):
        if self.find_element(self.timingEndDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_videoStartDialog(self):
        return self.is_feature_exist(self.videoStartDialog)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)
