#——————学习计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 计时页面点击结束
    timingEnd = By.XPATH, '//*[@text="结束"]'
    # 计时结算页弹窗【知道了】
    timingEndDialog = By.XPATH, '//*[@text="知道了"]'
    # 计时结算页右上角【完成】按钮
    timingEndSuccess = By.XPATH, '//*[@text="完成"]'
    #计时不足1min点击结束出现的弹窗_【确定】按钮
    timingEndConfirmRight = By.XPATH, '//*[@text="确定"]'
    #计时不足1min点击结束出现的弹窗_【取消】按钮
    timingEndConfirmLeft = By.XPATH, '//*[@text="取消"]'
    # 学习计时_时长设置按钮
    studySettingBtn = By.ID, 'com.huiian.timing:id/tv_setting_time_common'
    # 学习计时_时长设置完成
    studySettingsuccessBtn = By.XPATH, '//*[@text="完成"]'
    # 学习计时_开始学习按钮
    startTimingBtn = By.ID, 'com.huiian.timing:id/tv_confirm_common'


    # 第一次点击视频打开，出现视频录制权限弹窗
    videoStartDialog = By.XPATH, '//*[@text="始终允许"]'
    # 视频打卡结束后_分享视频打卡按钮
    videoSuccess = By.XPATH, '//*[@text="分享视频打卡"]'
    # 视频打卡页面开始学习按钮
    videoStartBtn = By.XPATH, '//*[@text="开始学习"]'
    # 视频打卡页面结束_确定按钮
    videoEndDialog = By.XPATH, '//*[@text="确定"]'
    # 学习目标输入框
    studyContentBox = By.ID, 'com.huiian.timing:id/et_common_title'

    # 番茄学习目标输入框
    tomatoContentBox = By.ID, 'com.huiian.timing:id/et_title'
    # 视频打卡目标输入框
    videoContentBox = By.ID, 'com.huiian.timing:id/et_title'
    # 番茄计时_开始学习按钮
    startTomatoBtn = By.XPATH, '//*[@text="开始学习"]'
    # 视频打卡_确定并开启摄像头按钮
    startVideoBtn = By.ID, 'com.huiian.timing:id/tv_confirm'

    # 睡觉时_分享弹窗中的关注按钮
    sleepingClose = By.ID, 'com.huiian.timing:id/close_iv'
    # 睡觉时_起床按钮
    sleepingWake = By.ID, 'com.huiian.timing:id/wake_tv'


    def click_timingDialog(self):
        self.click(self.timingDialog)
    def click_timingEnd(self):
        self.click(self.timingEnd)
    def click_timingEndDialog(self):
        self.click(self.timingEndDialog)
    def click_timingEndSuccess(self):
        self.click(self.timingEndSuccess)
    def click_videoStartDialog(self):
        self.click(self.videoStartDialog)
    def click_videoSuccess(self):
        self.click(self.videoSuccess)
    def click_videoStartBtn(self):
        self.click(self.videoStartBtn)
    def click_videoEndDialog(self):
        self.click(self.videoEndDialog)
    def click_studySettingBtn(self):
        self.click(self.studySettingBtn)
    def click_studySettingsuccessBtn(self):
        self.click(self.studySettingsuccessBtn)
    def click_startTimingBtn(self):
        self.click(self.startTimingBtn)
    def click_startTomatoBtn(self):
        self.click(self.startTomatoBtn)
    def click_startVideoBtn(self):
        self.click(self.startVideoBtn)
    def click_sleepingClose(self):
        self.click(self.sleepingClose)
    def click_sleepingWake(self):
        self.click(self.sleepingWake)
    def click_timingEndConfirmRight(self):
        self.click(self.timingEndConfirmRight)

    def input_studyContentBox(self,content):
        self.input(self.studyContentBox,content)
    def input_tomatoContentBox(self,content):
        self.input(self.tomatoContentBox,content)
    def input_videoContentBox(self, content):
        self.input(self.videoContentBox, content)

    def waitAndfind_timingEndSuccess(self):
        if self.waitLoading(self.timingEndSuccess, t=2) == True:
            return True
        else:
            return False

    def waitAndfind_timingEndConfirmLeft(self):
        if self.waitLoading(self.timingEndConfirmLeft, t=2) == True:
            return True
        else:
            return False

    def waitAndfind_videoSuccess(self):
        if self.waitLoading(self.videoSuccess, t=2) == True:
            return True
        else:
            return False

    def check_timingDialog(self):
        if self.find_element(self.timingDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_timingEndDialog(self):
        if self.find_element(self.timingDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_videoStartDialog(self):
        return self.is_feature_exist(self.videoStartDialog)

    def check_sleepingClose(self):
        if self.find_element(self.sleepingClose, timeout=2, poll=1) == "":
            return False
        else:
            return True