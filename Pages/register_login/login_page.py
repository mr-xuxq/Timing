#——————手机号/qq/微信登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login(BaseAction):
    # 【微信号登录】
    wechat = By.ID, 'com.huiian.timing:id/ll_lbw'
    # 【手机号登录】
    phone =By.ID,'com.huiian.timing:id/ll_lbp'
    # 【QQ号登录】
    qq = By.ID,'com.huiian.timing:id/ll_lbq'
    # 【隐私协议】
    privacyProtocol = By.ID,'com.huiian.timing:id/ll_lbq'

    def click_phone_login(self):
        self.click(self.phone)
    def click_QQ_login(self):
        self.click(self.qq)
    def click_wechat_login(self):
        self.click(self.wechat)
    def click_Privacy_protocol(self):
        self.click(self.privacyProtocol)