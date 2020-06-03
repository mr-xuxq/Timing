#——————手机号密码登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_forgetPwd(BaseAction):
    #【下一步】
    nextBtn =By.ID,'com.huiian.timing:id/tv_next'
    #【验证码输入框】
    captchaBox =By.ID,'com.huiian.timing:id/et_captcha'
    #【密码输入框】
    pwdBox =By.ID,'com.huiian.timing:id/et_password'
    #【完成按钮】
    finshBtn =By.ID,'com.huiian.timing:id/login_verify_tv'


    def input_captcha(self, content):
        self.input(self.captchaBox,content)

    def input_pwd(self, content):
        self.input(self.pwdBox,content)

    def click_nextBtn(self):
        self.click(self.nextBtn)

    def click_finshBtn(self):
        self.click(self.finshBtn)

    def back(self):
        self.press_back()

