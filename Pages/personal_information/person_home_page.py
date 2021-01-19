#——————个人主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Person_home(BaseAction):
    #修改资料按钮
    personInfo = By.XPATH,'//*[@text="修改资料"]'
    #认证图标
    authenIcon = By.ID,'com.huiian.timing:id/icon'
    #顶部用户名称
    nickName = By.ID,'com.huiian.timing:id/activity_banner_title_tv'
    #点击右上角分享按钮
    share = By.ID,'com.huiian.timing:id/iv_action'
    #TimingID
    timingID = By.ID,'com.huiian.timing:id/tv_timing_id'
    # 我的二维码
    MyQR_code = By.ID, 'com.huiian.timing:id/iv_qr_code'
    #点击复制timingID
    copyTimingID = By.ID,'com.huiian.timing:id/tv_timing_id'


    def click_personInfo(self):
        self.click(self.personInfo)
    def click_share(self):
        self.click(self.share)
    def click_timingID(self):
        self.click(self.timingID)
    def click_MyQR_code(self):
        self.click(self.MyQR_code)
    def click_copyTimingID(self):
        self.click(self.copyTimingID)

    def get_nickName(self):
        self.get_text(self.nickName)

    def waitAndfind_personInfo(self):
        if self.waitLoading(self.personInfo, t = 1) == True:
            return True
        else:
            return False
    def check_personInfo(self):
        return self.is_feature_exist(self.personInfo)
    def check_authenIcon(self):
        return self.is_feature_exist(self.authenIcon)