from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Video_room(BaseAction):
    # 【退出按钮】
    exitBtn = By.ID, 'com.huiian.timing:id/iv_live_room_exit'
    # 【关闭按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_close'
    # 【聊天按钮】
    msgBtn = By.ID, 'com.huiian.timing:id/tv_msg_trigger'
    # 【麦上座位按钮】
    micBtn = By.ID, 'com.huiian.timing:id/rl_mic_item'
    # 【退出视频按钮】
    leaveRoomBtn = By.ID, 'com.huiian.timing:id/ly_leave'
    # 【确定退出视频按钮】
    leaveYesBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_tv'



    def click_exit(self):
        self.click(self.exitBtn)

    def click_close(self):
        self.click(self.closeBtn)

    def click_msg(self):
        self.click(self.msgBtn)

    def click_mic(self):
        self.click(self.micBtn)

    def click_leaveRoom(self):
        self.click(self.leaveRoomBtn)

    def click_leaveYes(self):
        self.click(self.leaveYesBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)








