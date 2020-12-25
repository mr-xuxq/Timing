#——————消息页——————
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Message(BaseAction):
# 消息页面元素-------------------------------------------------------------
    # tab消息
    messageBtn = By.ID, 'com.huiian.timing:id/message_img'
    # Timing小书童
    timingService = By.XPATH, '//*[@text="Timing小书童"]'
    # 退出Timing小书童
    backBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_iv'
    # 互动通知
    interaction = By.XPATH, '//*[@text="互动通知"]'
    # 道友标志
    messageFriend = By.ID, 'com.huiian.timing:id/iv_friend'
    # 红点
    messagePoint = By.ID, 'com.huiian.timing:id/friend_msg_new_iv'
    #群组标志
    messageTeam = By.ID,'com.huiian.timing:id/team_type_iv'
    # 群名称：测试专用群
    specialGroup = By.XPATH, '//*[@text="测试专用群"]'
    # 置顶按钮
    setTopBtn = By.ID, 'com.huiian.timing:id/popupwindow_set_top_tv'
    # 文字消息
    textMessage = By.XPATH, '//*[@text="I am a message!"]'
    # 图片消息
    photoMessage = By.XPATH, '//*[@text="[图片]"]'
    # 视频消息
    videoMessage = By.XPATH, '//*[@text="[视频]"]'
    # 建群系统消息
    groupMessage = By.XPATH, '//*[@text="恭喜你~成功创建群"]'
    # 最新消息栏
    firstChannel = By.ID, 'com.huiian.timing:id/tv_content'

    #时间FU窗
    timeFloat=By.ID, 'com.huiian.timing:id/timing_minutes_tv'

    def click_messageBtn(self):
        self.click(self.messageBtn)

    def click_messageTeam(self):
        self.click(self.messageTeam)

    def click_timingService(self):
        self.click(self.timingService)

    def click_back(self):
        self.click(self.backBtn)

    def click_interaction(self):
        self.click(self.interaction)

    def click_messageFriend(self):
        self.click(self.messageFriend)

    def click_specialGroup(self):
        self.click(self.specialGroup)

    def click_messagePoint(self):
        self.click(self.messagePoint)

    def click_setTop(self):
        self.click(self.setTopBtn)

    def click_messageTeam02(self):
        self.click(self.groupMessage)

    def click_firstChannel(self):
        self.click(self.firstChannel)

    def click_timeFloat(self):
        self.click(self.timeFloat)

    #在规定时间内是否找到元素
    def waitAndfind_timingService(self):
        if self.waitLoading(self.timingService,t = 2) == True:
            return True
        else:
            return False

    #在规定时间内是否找到元素
    def waitAndfind_interaction(self):
        if self.waitLoading(self.interaction,t = 2) == True:
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
            return True

    def check_textMessage(self):
        if self.find_element(self.textMessage, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_photoMessage(self):
        if self.find_element(self.photoMessage, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_videoMessage(self):
        if self.find_element(self.videoMessage, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_groupMessage(self):
        if self.find_element(self.groupMessage, timeout=2, poll=1) == "":
            return False
        else:
            return True

    def check_timeFloat(self):
        return self.is_feature_exist(self.timeFloat)

    def get_followCount(self):
        count = self.driver.find_element_by_id('com.huiian.timing:id/friend_msg_content_tv').text
        return count

    #在消息页面找群组
    def waitAndfind_discussTeam(self):
        if self.waitLoading(self.messageTeam,t = 1) == True:
            return True
        else:
            return False