#——————长视频列表页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class List_sVlog(BaseAction):
    # 【后退按钮】
    backBtn = By.ID, 'com.huiian.timing:id/ivClose'
    # 【发布sVlog按钮】
    postsVlog = By.ID, 'com.huiian.timing:id/ivVlogPublish'
    # 【推荐】按钮
    recommendBtn = By.XPATH, '//*[@text="推荐"]'
    # 【关注】按钮
    followBtn = By.ID, 'com.huiian.timing:id/tv_follow'

    def click_back(self):
        self.click(self.backBtn)
    def click_postsVlog(self):
        self.click(self.postsVlog)
    def click_followBtn(self):
        self.click(self.followBtn)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,150)
    def swipeDown(self):
        self.swipeOperat(0.5, 0.2, 0.5, 0.8, 150)
    def swipeLeft(self):
        self.swipeOperat(0.8, 0.8, 0.2, 0.8, 800)
    def check_followBtn(self):
        return self.is_feature_exist(self.followBtn)