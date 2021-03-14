#—————————-首页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Shouye(BaseAction):
    # 【道友圈按钮】
    friendCircleBtn = By.ID, 'com.huiian.timing:id/iv_main_friend_feed'
    # 【搜索按钮】
    searchBtn = By.ID, 'com.huiian.timing:id/iv_main_search'
    # 首页【更多按钮】
    mainMoreBtn = By.ID, 'com.huiian.timing:id/iv_main_more'
    # 【约个学习局按钮】
    studyDeskBtn = By.ID, 'com.huiian.timing:id/layout_study_desk'
    # 【邀请道友按钮】
    inviteFriendBtn = By.ID, 'com.huiian.timing:id/layout_invite_friend'
    # 【消息页第一个Channel】
    channel = By.ID, 'com.huiian.timing:id/cl_content'
    # 【道友标签】
    friendIcon = By.ID, 'com.huiian.timing:id/iv_friend'
    # Timing小书童
    timingService = By.XPATH, '//*[@text="Timing小书童"]'
    # 互动通知
    interaction = By.XPATH, '//*[@text="互动通知"]'
    # 置顶按钮
    setTopBtn = By.ID, 'com.huiian.timing:id/popupwindow_set_top_tv'
    # 退出Timing小书童
    backBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_iv'
    # 【+开始学习按钮】
    startStudyBtn = By.ID, 'com.huiian.timing:id/layout_start_action'


    def click_friendCircle(self):
        self.click(self.friendCircleBtn)
    def click_searchBtn(self):
        self.click(self.searchBtn)
    def click_mainMoreBtn(self):
        self.click(self.mainMoreBtn)
    def click_studyDeskBtn(self):
        self.click(self.studyDeskBtn)
    def click_inviteFriendBtn(self):
        self.click(self.inviteFriendBtn)
    def click_channel(self):
        self.click(self.channel)
    def click_friendIcon(self):
        self.click(self.friendIcon)
    def click_timingService(self):
        self.click(self.timingService)
    def click_interaction(self):
        self.click(self.interaction)
    def click_setTopBtn(self):
        self.click(self.setTopBtn)
    def click_backBtn(self):
        self.click(self.backBtn)
    def click_startStudyBtn(self):
        self.click(self.startStudyBtn)
    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,1500)
    def swipeByShouye(self):
        self.swipeOperat(0.5, 0.8, 0.5, 0.2,500)
    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)
    def check_friendCircle(self):
        return self.is_feature_exist(self.friendCircleBtn)