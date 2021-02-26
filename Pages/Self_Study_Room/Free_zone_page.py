# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 17:17
# @Author  : Geng
# @File    : Free_zone_page.py
#—————————-免费区—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Free_zone(BaseAction):
    # 【返回按钮】
    returnBtn = By.ID, 'com.huiian.timing:id/iv_back'
    # 【快速加入按钮】
    quickjoinBtn = By.ID, 'com.huiian.timing:id/cl_support_header'
    # 【进入按钮】
    getintoBtn = By.ID, 'com.huiian.timing:id/btn_join_room'
    # 【付费区按钮】
    payzoneBtn = By.ID, 'com.huiian.timing:id/tv_item_title'


    def click_return(self):
        self.click(self.returnBtn)

    def click_quickjoin(self):
        self.click(self.quickjoinBtn)

    def click_getinto(self):
        self.click(self.getintoBtn)

    def click_payzone(self):
        self.click(self.payzoneBtn)

    # def swipeUp(self):
    #     self.swipeOperat(0.5,0.8,0.5,0.2,1500)
    #
    # def swipeByShouye(self):
    #     self.swipeOperat(0.5, 0.8, 0.5, 0.2,500)
    #
    # def tapScreen(self,x,y):
    #     L = self.getSize()
    #     self.driver.tap([(L[0]*x,L[1]*y)],1)

    # def waitAndFind(self):
    #     if  self.waitLoading(self.moreBtn,t=5) == True:
    #         return True
    #     else:
    #         return False
