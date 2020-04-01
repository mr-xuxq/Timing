from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Setting(BaseAction):
    # 【更多按钮】
    moreBtn = By.ID, 'com.huiian.timing:id/mine_img'
    # 【设置按钮】
    settingBtn = By.ID, 'com.huiian.timing:id/iv_setting'
    # 【退出登录按钮】
    logoutBtn = By.ID, 'com.huiian.timing:id/logout_tv'
    # 【确认退出登录按钮】
    confirmLogoutBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_tv'
    # 【目标】
    target = By.ID, 'com.huiian.timing:id/ll_lbp'


    def click_more(self):
        self.click(self.moreBtn)

    def click_setting(self):
        self.click(self.settingBtn)

    def click_logout(self):
        self.click(self.logoutBtn)

    def click_confirmLogout(self):
        self.click(self.confirmLogoutBtn)

    def findLogin(self):
        if self.waitLoading(self.target,t=5) == True:
            return True
        else:
            return False