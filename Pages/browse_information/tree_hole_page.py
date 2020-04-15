#—————————-树洞对讲机频道页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Tree_hole(BaseAction):
    # 【树洞对讲机按钮】
    treeHoleBtn = By.ID, 'com.huiian.timing:id/cl_entry'
    # 【自动寻呼按钮】
    matchHoleBtn = By.ID, 'com.huiian.timing:id/cl_auto_search'
    # 【允许按钮】
    allowBtn = By.ID, 'android:id/button1'
    # 【树洞频道】
    holeChannelBtn = By.ID, 'com.huiian.timing:id/intercom_current_fm_value'
    # 【切换频道按钮】
    switchChannelBtn = By.ID, 'com.huiian.timing:id/intercom_fm_change'



    def click_treeHole(self):
        self.click(self.treeHoleBtn)

    def click_matchHole(self):
        self.click(self.matchHoleBtn)

    def click_allowBtn(self):
        self.click(self.allowBtn)

    def click_switchChannelBtn(self):
        self.click(self.switchChannelBtn)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)

    def check_channel(self):
        return self.is_feature_exist(self.holeChannelBtn[1])