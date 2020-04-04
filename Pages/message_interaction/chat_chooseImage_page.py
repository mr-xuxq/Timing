#——————聊天选择图片页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Choose_image(BaseAction):
#发日记_选择照片页
    chooseImage = By.ID, 'com.huiian.timing:id/photo_list_item_index_tv'
    # 【下一步】
    nextStep = By.ID, 'com.huiian.timing:id/activity_banner_right_btn'
#上传头像_选择照片页
    chooseMyimg = By.ID,'com.huiian.timing:id/photo_list_item_img'
    #右下角_【选取】
    imgSummit = By.XPATH,'//*[@text="选取"]'
    #左下角_【取消】
    imgCancel = By.XPATH,'//*[@text="取消"]'

    def click_chooseImage(self,target):
        self.click(target)
