#！/usr/bin/env python
# -*- coding:utf-8 -*-
#个人主页的timingid and 二维码
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Share(BaseAction):
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
    # 返回按钮
    returnpersonal = By.ID, 'com.huiian.timing:id/iv_back'

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