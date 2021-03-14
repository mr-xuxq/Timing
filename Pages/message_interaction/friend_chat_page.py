#——————道友聊天页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Friend_chat(BaseAction):
    # 道友左上角【后退】按钮
    friendBack = By.ID, 'com.huiian.timing:id/iv_message_back'
    # 道友右上角【更多】按钮
    friendMore = By.ID, 'com.huiian.timing:id/iv_message_more'
    # 发送消息失败
    failSend = By.ID, 'com.huiian.timing: id/message_item_alert'
    # 道友页+按钮
    itemBtn = By.ID, 'com.huiian.timing:id/buttonMoreFuntionInText'
    # 道友页录制按钮
    recordBtn = By.ID, 'com.huiian.timing:id/iv_video_small'
    # 聊天页面输入框
    messageBox = By.ID, 'com.huiian.timing:id/editTextMessage'
    # 发送按钮
    messageSend = By.ID, 'com.huiian.timing:id/sendLayout'
    # 相册按钮
    imageBtn = By.XPATH,'//*[@text="相册"]'
    # 拍摄按钮
    shutterBtn = By.XPATH, '//*[@text="拍摄"]'
    # 视频按钮
    videoBtn = By.XPATH,'//*[@text="视频"]'

    def click_friendBack(self):
        self.click(self.friendBack)
    def click_friendMore(self):
        self.click(self.friendMore)
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
    def input_messageBox(self,content):
        self.input(self.messageBox,content)
