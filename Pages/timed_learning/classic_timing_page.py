#——————学习计时各类子页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Classic_timing(BaseAction):
    # 计时页面元素------------------------------------------------------------------------
    # 完成计时后弹窗【我知道了】
    timingDialog = By.XPATH, '//*[@text="我知道了"]'
    # 计时页面点击结束
    #timingEnd = By.XPATH, '//*[@text="结束"]'
    timingEnd = By.ID, 'com.huiian.timing:id/timing_finish_tv'
    # 计时页面暂停按钮
    timingPause = By.ID, 'com.huiian.timing:id/timing_pause_tv'
    # 计时页面继续按钮
    timingContinue = By.ID, 'com.huiian.timing:id/timing_continue_tv'
    # 计时页面继续按钮
    timingAgain_30 = By.ID, 'com.huiian.timing:id/tv_timing_again'
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
    #timingEndDialog = By.XPATH, '//*[@text="知道了"]'
    timingEndDialog = By.ID, 'com.huiian.timing:id/tv_know'
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

    # 学习计时_开始学习按钮
    startTimingBtn = By.ID, 'com.huiian.timing:id/tv_confirm_common'
    # 离开聊天室确认弹窗
    leaveChatroomYes = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'
    # 计时聊天消息气泡
    studyDiscussContent = By.ID, 'com.huiian.timing:id/tvContent'
    # 再次开始学习标签
    timingAgain = By.ID, 'com.huiian.timing:id/layout_timing_tv_study_restart'
# -----------------------------------------------------------------------------------------------------------------------
    def click_timingDialog(self):
        self.click(self.timingDialog)
    def click_timingEnd(self):
        self.click(self.timingEnd)
    def click_timingPause(self):
        self.click(self.timingPause)
    def click_timingContinue(self):
        self.click(self.timingContinue)
    def click_timingAgain_30(self):
        self.click(self.timingAgain_30)
    def click_timingAgain(self):
        self.click(self.timingAgain)
    def click_timingEndYes(self):
        self.click(self.timingEndYes)
    def click_timingEndDialog(self):
        self.click(self.timingEndDialog)
    def click_timingEndSuccess(self):
        self.click(self.timingEndSuccess)
    def click_studySettingBtn(self):
        self.click(self.studySettingBtn)

    def click_startTimingBtn(self):
        self.click(self.startTimingBtn)
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

    def input_sendWordBox(self,content):
        self.input(self.sendWordBox,content)
#-----------------------------------------------------------------------------------------------------------------------
    def waitAndfind_timingEndConfirmLeft(self):
        if self.waitLoading(self.timingEndConfirmLeft, t=2) == True:
            return True
        else:
            return False
#------------------------------------------------------------------------------------------------------------------------
    def check_timingDialog(self):
        if self.find_element(self.timingDialog,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_timingEndSuccess(self):
        return self.is_feature_exist(self.timingEndSuccess)
    def check_timingEndDialog(self):
        return self.is_feature_exist(self.timingEndDialog)
    def check_todayLearningTime(self):
        return self.is_feature_exist(self.todayLearningTime)
    def check_leaveChatroomYes(self):
        return self.is_feature_exist(self.leaveChatroomYes)
    def check_studyDiscussContent(self):
        return self.is_feature_exist(self.studyDiscussContent)
    def check_timingAgain(self):
        return self.is_feature_exist(self.timingAgain)
    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)
