#——————聊天页面选择照片页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class ChooseVideo(BaseAction):

    # 【下一步】
    nextStep = By.ID, 'com.huiian.timing:id/activity_banner_right_btn'
    # 选中视频
    chooseVideo = By.ID, 'com.huiian.timing:id/video_item_img'

    def click_chooseVideo(self,target):
        self.click(target)
