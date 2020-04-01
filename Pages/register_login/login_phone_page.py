#——————验证码登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_phone(BaseAction):
    #手机号登录页-右上角【密码登录】
    loginByPwd =By.ID,'com.huiian.timing:id/activity_banner_right_tv'
    #手机号登录页-左上角【X】按钮
    Back =By.ID,'com.huiian.timing:id/activity_banner_back_iv'
    #手机号登录页-【手机号输入框】
    phoneBox =By.ID,'com.huiian.timing:id/phone_et'
    #手机号登录页-【获取验证码】按钮
    getCaptcha =By.ID,'com.huiian.timing:id/login_verify_tv'
    #手机号登录页-【登录遇到问题】按钮
    problemWhileLogin =By.ID,'com.huiian.timing:id/tv_login_problem'

    def click_loginByPwd(self):
        self.click(self.loginByPwd)
    def input_phone(self, content):
        self.input(self.phoneBox,content)
    def back(self):
        self.press_back()
    def click_getCaptcha(self):
        self.click(self.getCaptcha)
    def click_problemWhileLogin(self):
        self.click(self.problemWhileLogin)