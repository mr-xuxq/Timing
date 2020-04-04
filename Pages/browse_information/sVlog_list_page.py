#——————长视频列表页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class List_sVlog(BaseAction):
    # 【后退按钮】
    backBtn = By.ID, 'com.huiian.timing:id/iv_back'
    # 【目标-sVlog标题】
    target = By.ID, 'com.huiian.timing:id/tv_content_vloglist'


    def click_back(self):
        self.click(self.backBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)


    def waitAndFind(self):
        if  self.waitLoading(self.target,t=5) == True:
            return True
        else:
            return False
