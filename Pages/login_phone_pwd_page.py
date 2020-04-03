#——————手机号密码登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_phone_pwd(BaseAction):
    #手机号输入框
    phone_password_home_phone =By.ID,'com.huiian.timing:id/et_phone'
    #密码输入框
    phone_password_home_pwh =By.ID,'com.huiian.timing:id/et_password'
    #【登录】
    phone_password_home_login =By.ID,'com.huiian.timing:id/tv_login_verify'

    phone = '10000000405'
    password = '111111'

    def input_home_phone(self, content):
        self.input(self.phone_password_home_phone,content)

    def input_home_pwh(self, content):
        self.input(self.phone_password_home_pwh,content)

    def click_home_login(self):
        self.click(self.phone_password_home_login)

    def back(self):
        self.press_back()

    def waitAndfind(self,target,t):
        if self.waitLoading(target,t) == True:
            return True
        else:
            return False
