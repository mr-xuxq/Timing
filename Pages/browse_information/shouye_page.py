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
    # 【搜索】
    searchBtn = By.ID, 'com.huiian.timing:id/searching_header'
    # 【右上角+】
    plusBtn = By.ID, 'com.huiian.timing:id/iv_main_action_add'
    # 【live卡片】
    liveBtn = By.ID , 'com.huiian.timing:id/iv_live_str'
    # 【契约卡片】
    contractBtn = By.ID , 'com.huiian.timing:id/tv_contract_theme'
    # 【打卡卡片】
    dakaBtn = By.ID , 'com.huiian.timing:id/tv_clock_theme'
    # 【汤视频卡片】
    tang_videoBtn = By.ID , 'com.huiian.timing:id/iv_soup_vlog'
    # 【话题卡片】
    topicBtn = By.ID , 'com.huiian.timing:id/bg_topic_top'
    # # 【图文卡片】
    # tang_videoBtn = By.ID , 'com.huiian.timing:id/iv_soup_vlog'
    # # 【视频卡片】
    # topicBtn = By.ID , 'com.huiian.timing:id/bg_topic_top'




    # 【树洞对讲机按钮】
    treeHoleBtn = By.ID, 'com.huiian.timing:id/cl_entry'
    # 【自习室按钮】
    videoRoomBtn = By.ID, 'com.huiian.timing:id/cl_zxs_entrance'


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

    def click_search(self):
        self.click(self.searchBtn)

    def click_plus(self):
        self.click(self.plusBtn)

    def click_live(self):
        self.click(self.liveBtn)

    def click_contract(self):
        self.click(self.contractBtn)

    def click_daka(self):
        self.click(self.dakaBtn)

    def click_tang_video(self):
        self.click(self.tang_videoBtn)

    def click_topic(self):
        self.click(self.topicBtn)






    def click_treeHole(self):
        self.click(self.treeHoleBtn)

    def click_videoRoom(self):
        self.click(self.videoRoomBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,1500)


    def swipeByShouye(self):
        self.swipeOperat(0.5, 0.8, 0.5, 0.2,500)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)

    def waitAndFind(self):
        if  self.waitLoading(self.moreBtn,t=5) == True:
            return True
        else:
            return False

    def check_live(self):
        return self.is_feature_exist(self.liveBtn)

    def check_tang_video(self):
        return self.is_feature_exist(self.tang_videoBtn)

    def check_topic(self):
        return self.is_feature_exist(self.topicBtn)