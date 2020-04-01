from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class VideoHall(BaseAction):
    # 【值日班长标签】
    SPlabel = By.ID, 'com.huiian.timing:id/tv_supporter_notice'


    def waitAndFind(self):
        if  self.waitLoading(self.SPlabel,t=5) == True:
            return True
        else:
            return False







