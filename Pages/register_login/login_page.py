#——————手机号/qq/微信登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login(BaseAction):
    # 【手机定位权限_允许】
    allowLocation = By.ID, 'android:id/button1'
    # 【跳过按钮】
    ignoreBtn = By.ID, 'com.huiian.timing:id/tv_next'
    # 【微信号登录】
    wechat = By.ID, 'com.huiian.timing:id/ll_lbw'
    # 【手机号登录】
    phone =By.ID,'com.huiian.timing:id/ll_lbp'
    # 【QQ号登录】
    qq = By.ID,'com.huiian.timing:id/ll_lbq'
    # 【隐私协议】
    privacyProtocol = By.ID,'com.huiian.timing:id/ll_lbq'

    def check_phone(self):
        return  self.find_element(self.phone,timeout=2, poll=1)
    def check_location(self):
        return  self.find_element(self.allowLocation,timeout=2, poll=1)
    def click_allowLocation(self):
        self.click(self.allowLocation)
    def click_agree(self):
        L = self.getSize()
        self.driver.tap([(L[0]* 0.69, L[1]* 0.73)],1)
    def click_ignore(self):
        self.click(self.ignoreBtn)
    def click_phone_login(self):
        self.click(self.phone)
    def click_QQ_login(self):
        self.click(self.qq)
    def click_wechat_login(self):
        self.click(self.wechat)
    def click_Privacy_protocol(self):
        self.click(self.privacyProtocol)