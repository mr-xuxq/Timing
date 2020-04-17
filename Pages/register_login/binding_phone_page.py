#——————绑定手机页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Banding_phone(BaseAction):
    # 【关闭按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_back'
    # 【跳过按钮】
    ignoreBtn = By.ID, 'com.huiian.timing:id/tv_right'
    # 【手机号输入框】
    phoneBox = By.ID, 'com.huiian.timing:id/et_phone'
    # 【下一步按钮】
    nextBtn = By.ID, 'com.huiian.timing:id/tv_login_verify'


    def click_closeBtn(self):
        self.click(self.closeBtn)

    def click_ignoreBtn(self):
        self.click(self.ignoreBtn)

    def click_nextBtn(self):
        self.click(self.nextBtn)

    def input_phone(self, content):
        self.input(self.phoneBox,content)

    # 判断是否进入了绑定手机号页面

    def check_bingdingPhone(self):
        return self.is_feature_exist(self.ignoreBtn)

