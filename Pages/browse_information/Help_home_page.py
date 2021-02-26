# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 16:40
# @Author  : Geng
# @File    : Help_home_page.py
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Help_home(BaseAction):
    # 【live判断-首页按钮】
    pictureBtn = By.ID, 'com.huiian.timing:id/view_sp'
    # 【汤视频-log图标】
    iconBtn = By.ID, 'com.huiian.timing:id/ivLogo'
    # 【搜索页判断-今日牛人榜】
    manlistBtn = By.ID, 'com.huiian.timing:id/cl_search_famous'
    # 【话题页--+参与话题】
    participationtopicsBtn = By.ID, 'com.huiian.timing:id/study_diary_post_img'
    def check_picture(self):
        return self.is_feature_exist(self.pictureBtn)
    def check_icon(self):
        return self.is_feature_exist(self.iconBtn)
    def check_manlist(self):
        return self.is_feature_exist(self.manlistBtn)
    def check_participationtopics(self):
        return self.is_feature_exist(self.participationtopicsBtn)