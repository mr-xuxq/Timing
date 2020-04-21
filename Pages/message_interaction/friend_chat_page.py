#——————道友聊天页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Friend_chat(BaseAction):
    # 道友右上角【更多】按钮
    friendMore = By.ID, 'com.huiian.timing:id/team_history_fl'
    # 群组右上角【更多】按钮
    groupMore = By.ID, 'com.huiian.timing:id/iv_more'
    # 群组成员动态
    groupActive = By.XPATH, '//*[@text="成员动态"]'
    # 契约群-【群聊】
    groupChat = By.XPATH, '//*[@text="群聊"]'
    # 发送消息失败
    failSend = By.ID, 'com.huiian.timing: id/message_item_alert'
    # 道友页后退按钮
    backBtn = By.ID, 'com.huiian.timing:id/team_back_fl'
    # 群组页后退按钮
    backTeamBtn = By.ID, 'com.huiian.timing:id/iv_back'
    # 聊天页面输入框
    messageBox = By.ID, 'com.huiian.timing:id/editTextMessage'
    # 发送
    messageSend = By.ID, 'com.huiian.timing:id/buttonSendMessage'
    #选择发布的内容类型
    chooseType = By.ID,'com.huiian.timing:id/buttonMoreFuntionInText'
    #相册按钮
    imageBtn = By.XPATH,'//*[@text="相册"]'
    #视频按钮
    videoBtn = By.XPATH,'//*[@text="视频"]'


    def input_messageBox(self,content):
        self.input(self.messageBox,content)

    def click_messageSend(self):
        self.click(self.messageSend)
    def click_chooseType(self):
        self.click(self.chooseType)
    def click_groupMore(self):
        self.click(self.groupMore)
    def click_groupActive(self):
        self.click(self.groupActive)
    def click_groupChat(self):
        self.click(self.groupChat)
    def click_back(self):
        self.click(self.backBtn)
    def click_backTeam(self):
        self.click(self.backTeamBtn)
    def click_messageBox(self):
        self.click(self.messageBox)

    def click_imageBtn(self):
        self.click(self.imageBtn)

    def click_videoBtn(self):
        self.click(self.videoBtn)

        # 在规定时间内是否找到元素
    def waitAndfind_failSend(self):
        if self.waitLoading(self.failSend, t=1) == True:
            return True
        else:
            return False

    def check_groupMore(self):
        if self.find_element(self.groupMore, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_groupChat(self):
        if self.find_element(self.groupChat,timeout=2, poll=1) == "":
            return False
        else:
            return True

    def swipeByGroup(self):
        self.swipeOperat(0.5, 0.9, 0.5, 0.4, 500)

