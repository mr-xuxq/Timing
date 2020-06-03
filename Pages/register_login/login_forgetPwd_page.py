#�������������ֻ��������¼ҳ�桪����������#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login_forgetPwd(BaseAction):
    #����һ����
    nextBtn =By.ID,'com.huiian.timing:id/tv_next'
    #����֤�������
    captchaBox =By.ID,'com.huiian.timing:id/et_captcha'
    #�����������
    pwdBox =By.ID,'com.huiian.timing:id/et_password'
    #����ɰ�ť��
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

