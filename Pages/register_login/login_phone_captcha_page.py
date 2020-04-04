#——————手机号验证码登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_phone_captcha(BaseAction):
    # 验证码输入框
    captchaBox =By.ID,'com.huiian.timing:id/captcha_et'
    # 【完成】
    completeBtn =By.ID,'com.huiian.timing:id/login_verify_tv'
    # 【目标】
    target =By.ID, 'com.huiian.timing:id/message_img'

    def input_captcha(self, content):
        self.input(self.captchaBox,content)

    def click_loginBtn(self):
        self.click(self.completeBtn)

    def back(self):
        self.press_back()

    def waitAndFind(self):
        if  self.waitLoading(self.target,t=20) == True:
            return True
        else:
            return False

