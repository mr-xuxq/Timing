#——————进入学习计时前的页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 第一次点击视频打开，出现视频录制权限弹窗
    videoStartDialog = By.XPATH, '//*[@text="允许"]'

    # 道友结伴按钮
    friendTimeBtn = By.ID, 'com.huiian.timing:id/tv_study_online'

    # 自律工具
    studyTools = By.ID, 'com.huiian.timing:id/tv_study_tool'
    # 普通计时
    normalTiming = By.ID, 'com.huiian.timing:id/tv_study_record'
    # 视频打卡
    videoTiming = By.ID, 'com.huiian.timing:id/tv_video_dk'
    # 学习农场
    farmTiming = By.ID, 'com.huiian.timing:id/tv_learning_farm'
    # 后退按钮
    backBtn = By.ID, 'com.huiian.timing:id/iv_back'


    # 【学习目标】输入框{除普通计时}
    learningTargetBox = By.ID, 'com.huiian.timing:id/et_title'
    # 【学习目标】输入框-普通计时
    normalLearningTargetBox = By.ID, 'com.huiian.timing:id/et_common_title'

    # 【时长设置】按钮{普通计时除外}
    timeSettingBtn = By.ID, 'com.huiian.timing:id/tv_setting_time'
    # 【时长设置】按钮-普通计时
    studySettingBtn = By.ID, 'com.huiian.timing:id/tv_setting_time_common'


    # 时长设置【完成】-普通计时
    studySettingsuccessBtn = By.XPATH, '//*[@text="完成"]'
    # 时长设置【完成】{普通计时除外}
    settingFinshBtn = By.ID, 'com.huiian.timing:id/common_confirm_tv'

    # 【开始学习】按钮{普通计时除外}
    startLearningBtn = By.ID, 'com.huiian.timing:id/tv_confirm'
    # 【学习计时】按钮-普通计时
    startTimingBtn = By.ID, 'com.huiian.timing:id/tv_confirm_common'

    # 睡觉时_分享弹窗中的关闭按钮
    sleepingClose = By.ID, 'com.huiian.timing:id/close_iv'
    # 睡觉时_起床按钮
    sleepingWake = By.ID, 'com.huiian.timing:id/tv_up_sleep'
    # 起床按钮
    wakeBtn = By.ID, 'com.huiian.timing:id/wake_tv'
    # 起床时_生成卡片
    getupCard = By.ID, 'com.huiian.timing:id/status_dk_img'

    def click_timingDialog(self):
        self.click(self.timingDialog)
    def click_videoStartDialog(self):
        self.click(self.videoStartDialog)
    def click_startLearningBtn(self):
        self.click(self.startLearningBtn)
    def click_sleepingClose(self):
        self.click(self.sleepingClose)
    def click_sleepingWake(self):
        self.click(self.sleepingWake)
    def click_wakeBtn(self):
        self.click(self.wakeBtn)
    def click_timeSettingBtn(self):
        self.click(self.timeSettingBtn)
    def click_settingFinshBtn(self):
        self.click(self.settingFinshBtn)
    def click_studySettingsuccessBtn(self):
        self.click(self.studySettingsuccessBtn)
    def click_studySettingBtn(self):
        self.click(self.studySettingBtn)
    def click_startTimingBtn(self):
        self.click(self.startTimingBtn)
    def click_studyTools(self):
        self.click(self.studyTools)
    def click_normalTiming(self):
        self.click(self.normalTiming)
    def click_videoTiming(self):
        self.click(self.videoTiming)
    def click_farmTiming(self):
        self.click(self.farmTiming)
    def click_back(self):
        self.click(self.backBtn)
    def click_friendTimeBtn(self):
        self.click(self.friendTimeBtn)

    def press_back(self):
        self.press_back()

    def input_normalLearningTargetBox(self,content):
        self.input(self.normalLearningTargetBox,content)
    def input_learningTargetBox(self,content):
        self.input(self.learningTargetBox,content)

    def check_studySettingsuccessBtn(self):
        return self.is_feature_exist(self.studySettingsuccessBtn)
    def check_videoStartDialog(self):
        return self.is_feature_exist(self.videoStartDialog)
    def check_getupCard(self):
        return self.is_feature_exist(self.getupCard)
    def check_timingDialog(self):
        if self.find_element(self.timingDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True
    def check_sleepingClose(self):
        if self.find_element(self.sleepingClose, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)