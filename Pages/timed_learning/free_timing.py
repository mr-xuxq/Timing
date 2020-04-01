#——————手机号/qq/微信登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Shouye(BaseAction):
    # 【目标】
    target = By.ID, 'com.huiian.timing:id/message_img'

    def swipe_up(self):
        self.swipeOperat(x1=0.5,y1=0.8,x2=0.5,y2=0.2,t=500)

    def waitAndFind(self):
        if self.waitLoading(self.target, t=5) == True:
            return True
        else:
            return False