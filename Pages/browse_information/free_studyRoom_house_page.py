#——————免费自习室房间页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Free_studyRoom_house(BaseAction):
    # 【关闭按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_close'
    # 【消息输入框】
    msgBox = By.ID, 'com.huiian.timing:id/tv_content'
    # 【上麦按钮】
    joinSeat = By.ID, 'com.huiian.timing:id/tv_audience_micro'
    # 【自习室温馨提示】
    kindlyReminder = By.ID, 'com.huiian.timing:id/fl_message_item_body'
    # 【计时器】
    timeClock = By.ID, 'com.huiian.timing:id/rl_record'
    # 【上传图片】按钮
    sendPhoto = By.ID, 'com.huiian.timing:id/iv_select'

    def click_close(self):
        self.click(self.closeBtn)
    def click_msgBox(self):
        self.click(self.msgBox)
    def click_joinSeat(self):
        self.click(self.joinSeat)
    def click_sendPhoto(self):
        self.click(self.sendPhoto)
    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)
    def check_followBtn(self):
        return self.is_feature_exist(self.kindlyReminder)
    def check_timeClock(self):
        return self.is_feature_exist(self.timeClock)
    def input_msgBox(self,context):
        self.input(self.msgBox,context)







