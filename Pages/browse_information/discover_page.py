#——————发现页——————#
#coding:utf-8
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Discover(BaseAction):
    # 【关注页】
    followPage = By.XPATH, '//*[@text="关注"]'
    # 【学习Live】
    discoverPage = By.XPATH, '//*[@text="发现"]'
    # 【学习Live】
    studyRoom = By.XPATH, '//*[@text="自习室"]'
    # 【发布按钮】
    postBtn = By.ID, 'com.huiian.timing:id/iv_post'
    # 【发布视频按钮】
    postVideoDiaryBtn = By.ID, 'com.huiian.timing:id/iv_post_video_diary'
    # 【发布图文按钮】
    postPhotoDiaryBtn = By.ID, 'com.huiian.timing:id/iv_post_diary'
    # 【关闭发布按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_post_close'
    # 【精准匹配按钮】
    matchFriendBtn = By.ID, 'com.huiian.timing:id/iv_main_action_match_friend'
    # 【关闭道友圈按钮】
    closeFriendCircleBtn = By.ID, 'com.huiian.timing:id/iv_close'
    # 【目标-sVlog作者】
    sVlogAuthor = By.ID, 'com.huiian.timing:id/tv_vlog_user_name'
    # 【sVlog预览区】
    sVlogGif = By.ID, 'com.huiian.timing:id/iv_soup_vlog'

    def click_followPage(self):
        self.click(self.followPage)
    def click_discoverPage(self):
        self.click(self.discoverPage)
    def click_studyRoom(self):
        self.click(self.studyRoom)
    def click_postBtn(self):
        self.click(self.postBtn)
    def click_postVideoDiaryBtn(self):
        self.click(self.postVideoDiaryBtn)
    def click_postPhotoDiaryBtn(self):
        self.click(self.postPhotoDiaryBtn)
    def click_closeBtn(self):
        self.click(self.closeBtn)
    def click_matchFriendBtn(self):
        self.click(self.matchFriendBtn)
    def click_closeFriendCircleBtn(self):
        self.click(self.closeFriendCircleBtn)
    def click_sVlogGif(self):
        self.click(self.sVlogGif)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,150)
    def swipeDown(self):
        self.swipeOperat(0.5, 0.2, 0.5, 0.8, 150)
    def swipeLeft(self):
        self.swipeOperat(0.8, 0.8, 0.2, 0.8, 800)
    def check_sVlogAuthor(self):
        return self.is_feature_exist(self.sVlogAuthor)