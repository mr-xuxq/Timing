from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Shouye(BaseAction):
    # 【sVlog标题按钮】
    sVlogBtn = By.ID, 'com.huiian.timing:id/tv_svlog_title'


    def click_sVlog(self):
        self.click(self.sVlogBtn)

