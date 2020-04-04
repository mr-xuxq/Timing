#——————新手引导页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Guide(BaseAction):
    # 全流程【好的/下一步按钮】
    yesBtn = By.ID, 'com.huiian.timing:id/guide_next_page_tv'
    # 全流程【暂时不要按钮】
    noBtn = By.ID, 'com.huiian.timing:id/guide_next_module_tv'
    # 第一步【打招呼按钮】
    helloBtn = By.ID, 'com.huiian.timing:id/say_hello_tv'
    # 第一步【再了解组团学习按钮】
    groupTolearnBtn = By.ID, 'com.huiian.timing:id/change_found_firend_tv'
    # 第二步【群组按钮】
    groupBtn = By.ID, 'com.huiian.timing:id/team_infor_ll'


    def click_yesBtn(self):
        self.click(self.yesBtn)
    def click_noBtn(self):
        self.click(self.noBtn)
    def click_helloBtn(self):
        self.click(self.helloBtn)
    def click_groupTolearnBtn(self):
        self.click(self.groupTolearnBtn)
    def click_groupBtn(self):
        self.click(self.groupBtn)