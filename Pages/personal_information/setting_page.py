#——————设置页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Setting(BaseAction):
    # 【退出登录按钮】
    logoutBtn = By.ID, 'com.huiian.timing:id/logout_tv'
    # 【确认退出登录按钮】
    confirmLogoutBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_tv'
    # 【目标】
    target = By.ID, 'com.huiian.timing:id/ll_lbp'


    def click_logout(self):
        self.click(self.logoutBtn)

    def click_confirmLogout(self):
        self.click(self.confirmLogoutBtn)

    def check_target(self):
        return self.is_feature_exist(self.target)