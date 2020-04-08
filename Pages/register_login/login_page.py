#——————手机号/qq/微信登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Login(BaseAction):
    # 【手机定位权限_允许】
    allowLocation = By.ID, 'android:id/button1'
    # 【跳过按钮】
    ignoreBtn = By.ID, 'com.huiian.timing:id/tv_next'
    # 【微信号登录】
    wechatBtn = By.ID, 'com.huiian.timing:id/ll_lbw'
    # 【手机号登录】
    phoneBtn =By.ID,'com.huiian.timing:id/ll_lbp'
    # 【QQ号登录】
    qqBtn = By.ID,'com.huiian.timing:id/ll_lbq'
    # 【QQ授权登录按钮】
    qqAgreeBtn = By.XPATH, '//*[@text="QQ授权登录"]'
    # 【隐私协议】
    privacyProtocol = By.ID,'com.huiian.timing:id/ll_lbq'
    # 【目标】
    target =By.ID, 'com.huiian.timing:id/message_img'


    def check_phone(self):
        return  self.find_element(self.phoneBtn,timeout=2, poll=1)
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
        self.click(self.phoneBtn)
    def click_QQ_login(self):
        self.click(self.qqBtn)
    def click_QQ_agree(self):
        self.click(self.qqAgreeBtn)
    def click_wechat_login(self):
        self.click(self.wechatBtn)
    def click_Privacy_protocol(self):
        self.click(self.privacyProtocol)
    def waitAndFind(self):
        if  self.waitLoading(self.target,t=20) == True:
            return True
        else:
            return False
