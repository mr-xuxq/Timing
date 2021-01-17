#！/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xinlan time:2021/1/17
#个人主页的timingid and 二维码
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Share_personal(BaseAction):
    #更多按钮
    morebuttons = By.ID,'com.huiian.timing:id/mine_img'
    #点击进入个人主页
    personalinfo = By.ID,'com.huiian.timing:id/iv_go'
    #点击id
    timingID = By.ID,'com.huiian.timing:id/tv_timing_id'

    #点击右上角分享按钮
    share = By.ID,'com.huiian.timing:id/iv_action'


    #分享到微信好友
    wechatfriends = By.ID,'com.huiian.timing:id/ll_share_wechat'
    #分享到朋友圈
    wechatmoments = By.ID,'com.huiian.timing:id/ll_share_moment'
    #分享到QQ空间
    QQzone = By.ID,'com.huiian.timing:id/ll_share_qzone'
    #分享到QQ好友
    QQfriends = By.ID,'com.huiian.timing:id/ll_share_qq'
    #分享到微博
    weibo = By.ID,'com.huiian.timing:id/ll_share_weibo'

    #分享到最近聊天
    recentchat = By.ID,'com.huiian.timing:id/listview_recent_chat'
    # 点击返回到个人主页
    returnpersonal = By.ID, 'com.huiian.timing:id/iv_back'
    # 点击我的二维码
    MyQR_code = By.ID, 'com.huiian.timing:id/iv_qr_code'
    #点击复制timingID
    copyID = By.ID,'com.huiian.timing:id/tv_timing_id'
    #点击分享二维码名片
    shareQR_code_card = By.ID,'com.huiian.timing:id/tv_share_timing'
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











    def click_more(self):
        self.click(self.morebuttons)
    def click_personalinfo(self):
        self.click(self.personalinfo)
    def click_timingID(self):
        self.click(self.timingID)

    def click_share(self):
        self.click(self.share)

    def click_returnpersonal(self):
        self.click(self.returnpersonal)
    def click_wechatfriends(self):
        self.click(self.wechatfriends)
    def click_wechatmoments(self):
        self.click(self.wechatmoments)
    def click_QQzone(self):
        self.click(self.QQzone)
    def click_QQfriends(self):
        self.click(self.QQfriends)
    def click_weibo(self):
        self.click(self.weibo)
    def click_recentchat(self):
        self.click(self.recentchat)

    def click_MyQR_code(self):
        self.click(self.MyQR_code)
    def click_copyID(self):
        self.click(self.copyID)
    def click_shareQR_code_card(self):
        self.click(self.shareQR_code_card)
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