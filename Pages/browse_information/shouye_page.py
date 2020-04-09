#—————————-首页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Shouye(BaseAction):
    # 【sVlog标题按钮】
    sVlogBtn = By.ID, 'com.huiian.timing:id/tv_svlog_title'
    # 【自习室按钮】
    videoRoomBtn = By.ID, 'com.huiian.timing:id/cl_zxs_entrance'
    #【首页tab按钮】
    shouyeBtn = By.ID, 'com.huiian.timing:id/learning_home_img'

    def click_sVlog(self):
        self.click(self.sVlogBtn)

    def click_videoRoom(self):
        self.click(self.videoRoomBtn)

    def click_shouyeBtn(self):
        self.click(self.shouyeBtn)

    def swipeByShouye(self):
        self.swipeOperat(0.5, 0.7, 0.5, 0.3, 1500)

    # 在规定时间内是否找到tab首页按钮
    def waitAndFind(self):
        if self.waitLoading(self.shouyeBtn, t = 5) == True:
            return True
        else:
            return False

