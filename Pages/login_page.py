#——————手机号/qq/微信登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login(BaseAction):
    #【手机号登录】
    phone =By.ID,'com.huiian.timing:id/ll_lbp'

    def click_phone_login(self):
        self.click(self.phone)
