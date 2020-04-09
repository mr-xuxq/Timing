#——————关注页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Follow(BaseAction):
    # 【已关注按钮】
    followedBtn = By.ID, 'com.huiian.timing:id/followed_myself_tv'
    #确定取消关注TA
    cancelFollowedRight = By.ID,'com.huiian.timing:id/popupwindow_confirm_right_fl'

    def cancel_followed(self):
        self.driver.click(self.followedBtn)
    def cancelFollowed_right(self):
        self.driver.click(self.cancelFollowedRight)