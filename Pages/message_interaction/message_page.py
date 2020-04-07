#——————消息页——————
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Message(BaseAction):
# 消息页面元素-------------------------------------------------------------
    # tab消息
    messageBtn = By.ID, 'com.huiian.timing:id/message_img'
    # Timing小书童
    timingService = By.XPATH, '//*[@text="Timing小书童"]'
    # 互动通知
    interaction = By.XPATH, '//*[@text="互动通知"]'
    # 道友标志
    messageFriend = By.ID, 'com.huiian.timing:id/iv_friend'
    # 红点
    messagePoint = By.ID, 'com.huiian.timing:id/friend_msg_new_iv'
    #群组标志
    messageTeam = By.ID,'com.huiian.timing:id/team_type_iv'

    def click_messageBtn(self):
        self.click(self.messageBtn)

    def click_timingService(self):
        self.click(self.timingService)

    def click_interaction(self):
        self.click(self.interaction)

    def click_messageFriend(self):
        self.click(self.messageFriend)

    def click_messagePoint(self):
        self.click(self.messagePoint)

    #在规定时间内是否找到元素
    def waitAndfind_timingService(self):
        if self.waitLoading(self.timingService,t = 1) == True:
            return True
        else:
            return False

    #在规定时间内是否找到元素
    def waitAndfind_interaction(self):
        if self.waitLoading(self.interaction,t = 1) == True:
            return True
        else:
            return False

    #在规定时间内是否找到元素
    def waitAndfind_messagePoint(self):
        if self.waitLoading(self.messagePoint,t = 1) == True:
            return True
        else:
            return False

    def swipeByMessage(self):
        self.swipeOperat(0.5, 0.7, 0.5, 0.3, 1500)

    def check_messageFriend(self):
        if self.find_element(self.messageFriend, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_messagePoint(self):
        if self.find_element(self.messagePoint, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_timingService(self):
        if self.find_element(self.timingService, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_interaction(self):
        if self.find_element(self.interaction, timeout=2, poll=1) == "":
            return False
        else:
            return True

    #检查是否存在群组，存在则点击，存在就滑动
    def check_messageTeam(self):
        if self.find_element(self.messageTeam, timeout=2, poll=1) == "":
            return False
        else:
            self.click(self.messageTeam)