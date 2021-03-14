#——————发现页——————#
#coding:utf-8
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Match_friend(BaseAction):
    # 【发布按钮】
    backBtn = By.ID, 'com.huiian.timing:id/mClose'

    def click_backBtn(self):
        self.click(self.backBtn)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,300)