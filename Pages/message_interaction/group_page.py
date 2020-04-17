#——————群组页——————
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Group(BaseAction):
    # 群内部的tab页
    groupTab = By.ID, 'com.huiian.timing:id/tv_tab_title'
    # tab群聊
    groupTalk = By.XPATH, '//*[@text="群聊"]'
    #【解散该群】按钮
    leaveGroupBtn = By.ID, 'com.huiian.timing:id/tv_leave_team'
    #二次确认弹窗【确定】按钮
    rightBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'

    def click_right(self):
        self.click(self.rightBtn)

    def click_leaveGroup(self):
        self.click(self.leaveGroupBtn)