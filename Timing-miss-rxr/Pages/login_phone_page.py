#——————验证码登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_phone(BaseAction):
    #验证码登录页-右上角【密码登录】
    phone_password =By.ID,'com.huiian.timing:id/activity_banner_right_tv'

    def click_password_login(self):
        self.click(self.phone_password)
