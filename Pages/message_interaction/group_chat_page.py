#——————道友聊天页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Group_chat(BaseAction):
    # 群组左上角【后退】按钮
    groupBack = By.ID, 'com.huiian.timing:id/iv_message_back'
    # 聊天页顶部【自习室】按钮
    groupStudyRoom = By.ID, 'com.huiian.timing:id/iv_message_more'
    # 道友右上角【群设置】按钮
    groupSetting = By.ID, 'com.huiian.timing:id/iv_message_more'
    # 发送消息失败
    failSend = By.ID, 'com.huiian.timing: id/message_item_alert'
    # 群组页+按钮
    itemBtn = By.ID, 'com.huiian.timing:id/buttonMoreFuntionInText'
    # 群组页录制按钮
    recordBtn = By.ID, 'com.huiian.timing:id/iv_video_small'
    # 聊天页面输入框
    messageBox = By.ID, 'com.huiian.timing:id/editTextMessage'
    # 发送按钮
    messageSend = By.ID, 'com.huiian.timing:id/sendLayout'
    # 相册按钮
    imageBtn = By.XPATH, '//*[@text="相册"]'
    # 拍摄按钮
    shutterBtn = By.XPATH, '//*[@text="拍摄"]'
    # 视频按钮
    videoBtn = By.XPATH, '//*[@text="视频"]'

    def click_groupBack(self):
        self.click(self.groupBack)
    def click_groupStudyRoom(self):
        self.click(self.groupStudyRoom)
    def click_groupSetting(self):
        self.click(self.groupSetting)
    def click_failSend(self):
        self.click(self.failSend)
    def click_itemBtn(self):
        self.click(self.itemBtn)
    def click_recordBtn(self):
        self.click(self.recordBtn)
    def click_messageBox(self):
        self.click(self.messageBox)
    def click_messageSend(self):
        self.click(self.messageSend)
    def click_imageBtn(self):
        self.click(self.imageBtn)
    def click_shutterBtn(self):
        self.click(self.shutterBtn)
    def click_videoBtn(self):
        self.click(self.videoBtn)
    def tapScreen(self, x, y):
        self.tapOperat(x, y)
    def swipeByGroup(self):
        self.swipeOperat(0.5, 0.9, 0.5, 0.4, 500)
    def input_messageBox(self, content):
        self.input(self.messageBox, content)
