#—————————-首页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Shouye(BaseAction):
    # 【首页按钮】
    shouyeBtn = By.ID, 'com.huiian.timing:id/tab_learning_home_ll'
    # 【关注页按钮】
    followBtn = By.ID, 'com.huiian.timing:id/tab_follow_ll'
    # 【发布页按钮】
    postBtn = By.ID, 'com.huiian.timing:id/ll_post'
    # 【消息页按钮】
    messageBtn = By.ID, 'com.huiian.timing:id/tab_message_ll'
    # 【更多页按钮】
    moreBtn = By.ID, 'com.huiian.timing:id/tab_mine_ll'
    # 【sVlog标题按钮】
    sVlogBtn = By.ID, 'com.huiian.timing:id/tv_svlog_title'
    # 【树洞对讲机按钮】
    treeHoleBtn = By.ID, 'com.huiian.timing:id/cl_entry'
    # 【自习室按钮】
    videoRoomBtn = By.ID, 'com.huiian.timing:id/cl_zxs_entrance'
    # 【没有更多数据】
    noMoreData = By.ID, 'com.huiian.timing:id/load_more_load_end_view'



    def click_shouye(self):
        self.click(self.shouyeBtn)

    def click_follow(self):
        self.click(self.followBtn)

    def click_post(self):
        self.click(self.postBtn)

    def click_message(self):
        self.click(self.messageBtn)

    def click_more(self):
        self.click(self.moreBtn)

    def click_sVlog(self):
        self.click(self.sVlogBtn)

    def click_treeHole(self):
        self.click(self.treeHoleBtn)

    def click_videoRoom(self):
        self.click(self.videoRoomBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)

    def swipeByShouye(self):
        self.swipeOperat(0.5, 0.8, 0.5, 0.2,500)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)

    def waitAndFind(self):
        if  self.waitLoading(self.shouyeBtn,t=5) == True:
            return True
        else:
            return False

    def check_shouye(self):
        return self.is_feature_exist(self.shouyeBtn[1])
    def check_sVlog(self):
        return self.is_feature_exist(self.sVlogBtn[1])
    def check_noMoreData(self):
        return self.is_feature_exist(self.noMoreData[1])