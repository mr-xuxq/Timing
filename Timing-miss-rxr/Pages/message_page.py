#——————聊天消息页和群——————
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
    # 道友标志
    messageDao = By.ID, 'com.huiian.timing:id/iv_friend'
    # 群内部的tab页
    groupTab = By.ID, 'com.huiian.timing:id/tv_tab_title'
    # tab群聊
    groupTalk = By.XPATH, '//*[@text="群聊"]'

    def click_message(self,target):
        self.click(target)

    #在规定时间内是否找到元素
    def waitAndfind(self,target,t):
        if self.waitLoading(target,t) == True:
            return True
        else:
            return False

    def swipeByMy(self,x1, y1, x2, y2, t):
        self.swipeOperat(x1, y1, x2, y2, t)








