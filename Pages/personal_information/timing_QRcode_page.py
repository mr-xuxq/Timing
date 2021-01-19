#！/usr/bin/env python
# -*- coding:utf-8 -*-
#个人主页的timingid and 二维码
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Timing_QRcode(BaseAction):

    #分享到微信
    share_weixin = By.ID,'com.huiian.timing:id/tv_wechat'
    #分享到朋友圈
    friendsquan =   By.ID,'com.huiian.timing:id/tv_pyq'
    #分享到qq
    share_qq = By.ID,'com.huiian.timing:id/tv_qq'
    #分享到微博
    share_weibo = By.ID,'com.huiian.timing:id/tv_weibo'
    #保存图片
    savepicture = By.ID,'com.huiian.timing:id/tv_download'
    #点击取消
    cancel = By.ID,'com.huiian.timing:id/tv_cancel'
    #点击返回
    returnback = By.ID,'com.huiian.timing:id/activity_back_ll'
    #点击分享二维码名片
    shareQR_code_card = By.ID,'com.huiian.timing:id/tv_share_timing'

    def click_share_weixin(self):
        self.click(self.share_weixin)
    def click_friendsquan(self):
        self.click(self.friendsquan)
    def click_share_qq(self):
        self.click(self.share_qq)
    def click_share_weibo(self):
        self.click(self.share_weibo)
    def click_savepicture(self):
        self.click(self.savepicture)
    def click_cancel(self):
        self.click(self.cancel)
    def click_returnback(self):
        self.click(self.returnback)
    def click_shareQR_code_card(self):
        self.click(self.shareQR_code_card)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)