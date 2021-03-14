#——————付费自习室——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Pay_studyRoom(BaseAction):
    # 【值日班长标签】
    SPlabel = By.ID, 'com.huiian.timing:id/tv_supporter_notice'
    # 【快速进入按钮】
    quicklyJoinBtn = By.ID, 'com.huiian.timing:id/iv_quickly_enter'
    # 【房间进入按钮】
    joinBtn = By.ID, 'com.huiian.timing:id/btn_enter_room'
    # 【知道了按钮】
    agreeBtn = By.XPATH, '//*[@text="知道了"]'

    def click_quicklyJoin(self):
        self.click(self.quicklyJoinBtn)

    def click_join(self):
        self.click(self.joinBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)

    def tapScreen(self,x,y):
        self.tapOperat(x,y)

    def coordinateClick(self):
        self.tapOperat(0.5,0.92)

    def check_label(self):
        return self.is_feature_exist(self.SPlabel)






