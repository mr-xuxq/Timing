from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Shouye(BaseAction):
    # 【sVlog标题按钮】
    sVlogBtn = By.ID, 'com.huiian.timing:id/tv_svlog_title'
    # 【自习室按钮】
    videoRoomBtn = By.ID, 'com.huiian.timing:id/cl_zxs_entrance'

    def click_sVlog(self):
        self.click(self.sVlogBtn)

    def click_videoRoom(self):
        self.click(self.videoRoomBtn)

