#—————————-树洞对讲机频道页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Tree_hole(BaseAction):
    # 【树洞对讲机按钮】
    treeHoleBtn = By.ID, 'com.huiian.timing:id/cl_entry'
    # 【树洞匹配按钮】
    matchHoleBtn = By.ID, 'com.huiian.timing:id/tv_mood_type'
    # 【树洞频道】
    holeChannelBtn = By.ID, 'com.huiian.timing:id/intercom_current_fm_value'



    def click_treeHole(self):
        self.click(self.treeHoleBtn)

    def click_matchHole(self):
        self.click(self.matchHoleBtn)


    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)


    def findChannel(self):
        if  self.waitLoading(self.holeChannelBtn,t=5) == True:
            return True
        else:
            return False