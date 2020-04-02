#——————学习计时和番茄计时——————#
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
    # 视频打卡目标输入框
    videoContentBox = By.ID, 'com.huiian.timing:id/et_title'
    # 学习计时_时长设置按钮
    studySettingBtn = By.ID, 'com.huiian.timing:id/tv_setting_time_common'
    # 学习计时_时长设置完成
    studySettingsuccessBtn = By.XPATH, '//*[@text="完成"]'
    # 学习计时_开始学习按钮
    startTimingBtn = By.ID, 'com.huiian.timing:id/tv_confirm_common'
    # 番茄计时_开始学习按钮
    startTomatoBtn = By.XPATH, '//*[@text="开始学习"]'
    # 视频打卡_确定并开启摄像头按钮
    startVideoBtn = By.ID, 'com.huiian.timing:id/tv_confirm'
    # 睡觉时_分享弹窗中的关注按钮
    sleepingClose = By.ID, 'com.huiian.timing:id/close_iv'
    # 睡觉时_起床按钮
    sleepingWake = By.ID, 'com.huiian.timing:id/wake_tv'

    # 在规定时间内是否找到元素
    def waitAndfind(self, target, t):
        if self.waitLoading(target, t) == True:
            return True
        else:
            return False

    def swipeByMy(self, x1, y1, x2, y2, t):
        self.swipeOperat(x1, y1, x2, y2, t)

    def click_timing(self, target):
        self.click(target)



