#——————学习计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 计时页面点击结束
    #timingEnd = By.XPATH, '//*[@text="结束"]'
    timingEnd = By.ID, 'com.huiian.timing:id/timing_stop_tv'
    # 计时页面暂停按钮
    timingPause = By.ID, 'com.huiian.timing:id/timing_pause_tv'
    # 计时页面继续按钮
    timingContinue = By.ID, 'com.huiian.timing:id/timing_continue_tv'
    # 计时页面继续按钮
    timingAgain = By.ID, 'com.huiian.timing:id/tv_timing_again'
    # 计时页面确定结束按钮
    timingEndYes = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_tv'
    # 邀请学习按钮
    studyTogetherBtn = By.ID, 'com.huiian.timing:id/timing_invite_tv'
    # 选择最近聊天人员
    selectFriend = By.ID, 'com.huiian.timing:id/tv_name'
    # 发送计时邀请按钮
    studyTogetherForwardBtn = By.ID, 'com.huiian.timing:id/iv_forward'
    # 计时讨论按钮
    studyDiscussBtn = By.ID, 'com.huiian.timing:id/ivDiscuss'
    # 计时讨论输入框
    sendWordBox = By.ID, 'com.huiian.timing:id/editTextMessage'
    # 计时聊天发送按钮
    studyDiscussSendBtn = By.ID, 'com.huiian.timing:id/sendLayout'
    # 退回计时聊天页
    backBtn = By.ID, 'com.huiian.timing:id/iv_start_video_record'
    # 计时结算页弹窗【知道了】
    timingEndDialog = By.XPATH, '//*[@text="知道了"]'
    # 计时结算页右上角【完成】按钮
    #timingEndSuccess = By.XPATH, '//*[@text="完成"]'
    timingEndSuccess = By.ID, 'com.huiian.timing:id/tv_finish'
    #计时不足1min点击结束出现的弹窗_【确定】按钮
    timingEndConfirmRight = By.XPATH, '//*[@text="确定"]'
    #计时不足1min点击结束出现的弹窗_【取消】按钮
    timingEndConfirmLeft = By.XPATH, '//*[@text="取消"]'
    #计时结算-今日学习时长
    todayLearningTime = By.ID, 'com.huiian.timing:id/tv_total_learntime'
    # 学习计时_时长设置按钮
    studySettingBtn = By.ID, 'com.huiian.timing:id/tv_setting_time_common'
    # 学习计时_时长设置完成
    studySettingsuccessBtn = By.XPATH, '//*[@text="完成"]'
    # 学习计时_开始学习按钮
    startTimingBtn = By.ID, 'com.huiian.timing:id/tv_confirm_common'
    # 离开聊天室确认弹窗
    leaveChatroomYes = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'
    # 计时聊天消息气泡
    studyDiscussContent = By.ID, 'com.huiian.timing:id/tvContent'




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
    # 番茄计时_取消按钮
    timingTomatoCancel = By.ID, 'com.huiian.timing:id/tomato_cancel_tv'

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
    def click_timingPause(self):
        self.click(self.timingPause)
    def click_timingContinue(self):
        self.click(self.timingContinue)
    def click_timingAgain(self):
        self.click(self.timingAgain)
    def click_timingEndYes(self):
        self.click(self.timingEndYes)
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
    def click_studyTogetherBtn(self):
        self.click(self.studyTogetherBtn)
    def press_back(self):
        self.press_back()
    def click_selectFriend(self):
        self.click(self.selectFriend)
    def click_studyTogetherForwardBtn(self):
        self.click(self.studyTogetherForwardBtn)
    def click_studyDiscussBtn(self):
        self.click(self.studyDiscussBtn)
    def click_studyDiscussSendBtn(self):
        self.click(self.studyDiscussSendBtn)
    def click_backBtn(self):
        self.click(self.backBtn)
    def click_timingTomatoCancel(self):
        self.click(self.timingTomatoCancel)
    def click_leaveChatroomYes(self):
        self.click(self.leaveChatroomYes)


    def input_studyContentBox(self,content):
        self.input(self.studyContentBox,content)
    def input_tomatoContentBox(self,content):
        self.input(self.tomatoContentBox,content)
    def input_videoContentBox(self, content):
        self.input(self.videoContentBox, content)
    def input_sendWordBox(self,content):
        self.input(self.sendWordBox,content)

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
        if self.find_element(self.timingEndDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_videoStartDialog(self):
        return self.is_feature_exist(self.videoStartDialog)

    def check_studySettingsuccessBtn(self):
        return self.is_feature_exist(self.studySettingsuccessBtn)

    def check_sleepingClose(self):
        if self.find_element(self.sleepingClose, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_todayLearningTime(self):
        return self.is_feature_exist(self.todayLearningTime)

    def check_leaveChatroomYes(self):
        return self.is_feature_exist(self.leaveChatroomYes)

    def check_studyDiscussContent(self):
        return self.is_feature_exist(self.studyDiscussContent)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)