# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 19:31
# @Author  : Geng
# @File    : Free_study_room_page.py
#—————————-免费自习室—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Free_study_room(BaseAction):
    # 【返回按钮】
    returnBtn = By.ID, 'com.huiian.timing:id/iv_back'
    # 【快速加入按钮】
    quickjoinBtn = By.ID, 'com.huiian.timing:id/iv_quickly_enter'
    # 【进入按钮】
    getintoBtn = By.ID, 'com.huiian.timing:id/btn_enter_room'
    # 【分享按钮】
    shareBtn = By.ID, 'com.huiian.timing:id/iv_share'
    #【自习室房间画面缩放按钮--说明是观众】
    zoomBtn = By.ID , 'com.huiian.timing:id/iv_share'
    # 【自习室房间画面观众按钮--说明进入房间】
    audienceBtn = By.ID , 'com.huiian.timing:id/tv_num'

    def click_return(self):
        self.click(self.returnBtn)

    def click_quickjoin(self):
        self.click(self.quickjoinBtn)

    def click_getinto(self):
        self.click(self.getintoBtn)

    def click_share(self):
        self.click(self.shareBtn)

    def check_zoom(self):
        return self.is_feature_exist(self.zoomBtn)

    def check_audience(self):
        return self.is_feature_exist(self.audienceBtn)

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
    #     if  self.waitLoading(self.zoomBtn,t=5) == True:
    #         return True
    #     else:
    #         return False
