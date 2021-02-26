#——————互动视频录制页——————#
#coding:utf-8
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Video_record(BaseAction):
    #说话就拍按钮
    speakBtn = By.ID, 'com.huiian.timing:id/iv_video_small'
    #后退按钮
    backBtn = By.ID, 'com.huiian.timing:id/iv_back'
    #切换摄像头按钮
    switchCamera = By.ID, 'com.huiian.timing:id/ll_camera_flip'
    #美颜按钮
    beautyBtn = By.ID, 'com.huiian.timing:id/ll_face_beauty'
    #顶部标题
    titleWord = By.ID, 'com.huiian.timing:id/tv_target_name_prefix'
    #发送对象
    sendTarget = By.ID, 'com.huiian.timing:id/tv_target_name'
    #初始引导文案
    guideWord = By.ID, 'com.huiian.timing:id/mGuideSelfIntroduction'
    #柠檬头滑动框
    beginToRecord = By.ID, 'com.huiian.timing:id/mSlideToggleView'
    #头套
    hatsBtn = By.ID, 'com.huiian.timing:id/effectsEmpty'
    #说话就拍准备状态文案
    readyToSpeak = By.ID, 'com.huiian.timing:id/tv_state_desc'
    #开始录制
    startRecord = By.ID, 'com.huiian.timing:id/begin_record'
#-----------------------------------------------------------------------------------------------------------------------

    def click_speakBtn(self):
        self.click(self.speakBtn)

    def click_back(self):
        self.click(self.backBtn)

    def click_titleWord(self):
        self.click(self.titleWord)

    def click_sendTarget(self):
        self.click(self.sendTarget)

    def click_switchCamera(self):
        self.click(self.switchCamera)

    def click_beautyBtn(self):
        self.click(self.beautyBtn)

    def click_guideWord(self):
        self.click(self.guideWord)

    def click_beginToRecord(self):
        self.click(self.beginToRecord)

    def click_hatsBtn(self):
        self.click(self.hatsBtn)

    def click_startRecord(self):
        self.click(self.startRecord)
#-----------------------------------------------------------------------------------------------------------------------

    def check_back(self):
        return self.is_feature_exist(self.backBtn)

    def check_titleWord(self):
        return self.is_feature_exist(self.titleWord)

    def check_sendTarget(self):
        return self.is_feature_exist(self.sendTarget)

    def check_switchCamera(self):
        return self.is_feature_exist(self.switchCamera)

    def check_beautyBtn(self):
        return self.is_feature_exist(self.beautyBtn)

    def check_guideWord(self):
        return self.is_feature_exist(self.guideWord)

    def check_beginToRecord(self):
        return self.is_feature_exist(self.beginToRecord)

    def check_hatsBtn(self):
        return self.is_feature_exist(self.hatsBtn)

    def check_readyToSpeak(self):
        return self.is_feature_exist(self.readyToSpeak)

    def check_all_elements(self):
            if self.check_back() == True:
                if self.check_titleWord() == True:
                    if self.check_sendTarget() == True:
                        if self.check_switchCamera() == True:
                            if self.check_beautyBtn() == True:
                                if self.check_guideWord() == True:
                                    if self.check_beginToRecord() == True:
                                        if self.check_hatsBtn() == True:
                                            return True
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
#-----------------------------------------------------------------------------------------------------------------------
    def swipeToSpeak(self):
        self.swipeOperat(0.20,0.85,0.57,0.85,1500)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)

