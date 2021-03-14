#——————个人主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Person_home(BaseAction):
    #修改资料按钮
    changeData = By.XPATH,'//*[@text="修改资料"]'
    #认证图标
    authenIcon = By.ID,'com.huiian.timing:id/icon'
    #顶部用户名称
    nickName = By.ID,'com.huiian.timing:id/activity_banner_title_tv'

    def click_changeData(self):
        self.click(self.changeData)
    def get_nickName(self):
        self.get_text(self.nickName)
    def check_authenIcon(self):
        return self.is_feature_exist(self.authenIcon)
    def check_nickName(self):
        return self.is_feature_exist(self.nickName)