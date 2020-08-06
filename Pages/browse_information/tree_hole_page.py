#—————————-树洞对讲机频道页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Tree_hole(BaseAction):
    # 【树洞对讲机按钮】
    treeHoleBtn = By.ID, 'com.huiian.timing:id/cl_entry'
    # 【树洞匹配按钮】
    matchHoleBtn = By.ID, 'com.huiian.timing:id/tv_mood_type'
<<<<<<< HEAD
=======
    # 【树洞收听按钮】
    listenHoleBtn = By.ID, 'com.huiian.timing:id/cl_listen'
>>>>>>> 78ef5ac86c52608068f40fecb91b0e3097a77cf2
    # 【自动寻呼按钮】
    autoMatchBtn = By.ID, 'com.huiian.timing:id/cl_auto_search'
    # 【树洞频道】
    holeChannelBtn = By.ID, 'com.huiian.timing:id/intercom_current_fm_value'
    # 【切换频道按钮】
    switchChannelBtn = By.ID, 'com.huiian.timing:id/intercom_fm_change'



    def click_treeHole(self):
        self.click(self.treeHoleBtn)

    def click_matchHole(self):
        self.click(self.matchHoleBtn)

<<<<<<< HEAD
=======
    def click_listenHole(self):
        self.click(self.listenHoleBtn)

>>>>>>> 78ef5ac86c52608068f40fecb91b0e3097a77cf2
    def click_autoMatch(self):
        self.click(self.autoMatchBtn)

    def click_switchChannelBtn(self):
        self.click(self.switchChannelBtn)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)

    def check_channel(self):
        return self.is_feature_exist(self.holeChannelBtn)