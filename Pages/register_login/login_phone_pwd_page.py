#——————手机号密码登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_phone_pwd(BaseAction):
    #手机号输入框
    phoneBox =By.ID,'com.huiian.timing:id/et_phone'
    #密码输入框
    pwdBox =By.ID,'com.huiian.timing:id/et_password'
    #【登录】
    loginBtn =By.ID,'com.huiian.timing:id/tv_login_verify'


    def input_phone(self, content):
        self.input(self.phoneBox,content)

    def input_pwd(self, content):
        self.input(self.pwdBox,content)

    def click_loginBtn(self):
        self.click(self.loginBtn)

    def back(self):
        self.press_back()

