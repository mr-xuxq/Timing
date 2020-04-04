#——————连麦房间大厅页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Video_hall(BaseAction):
    # 【值日班长标签】
    SPlabel = By.ID, 'com.huiian.timing:id/tv_supporter_notice'
    # 【快速进入按钮】
    quicklyJoinBtn = By.ID, 'com.huiian.timing:id/iv_quickly_enter'
    # 【房间进入按钮】
    joinBtn = By.ID, 'com.huiian.timing:id/btn_enter_room'

    #点击知道了按钮
    def coordinateClick(self):
        L = self.getSize()
        self.driver.tap(L[0]*0.5,L[1]*0.92)

    def click_quicklyJoin(self):
        self.click(self.quicklyJoinBtn)

    def click_join(self):
        self.click(self.joinBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)


    def waitAndFind(self):
        if  self.waitLoading(self.SPlabel,t=5) == True:
            return True
        else:
            return False







