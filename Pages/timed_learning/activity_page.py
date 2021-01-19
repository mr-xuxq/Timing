#——————活动页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Activity(BaseAction):
    # 活动页面元素------------------------------------------------------------------------
    # 后退按钮
    backBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_arrow_iv'


    def click_back(self):
        self.click(self.backBtn)


    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)