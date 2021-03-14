#——————通用_选择图片页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Choose_image(BaseAction):
    # 【后退按钮】
    backBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_ll'
    # 【下一步】
    nextStep = By.ID, 'com.huiian.timing:id/activity_banner_right_btn'
    # 【选择第一张图片】
    choosePhoto = By.ID,'com.huiian.timing:id/photo_list_item_index_tv'
    # 【相机按钮】
    cameraBtn = By.ID,'com.huiian.timing:id/hint'
    # 【拍摄按钮】
    shutterBtn = By.ID,'com.android.camera:id/shutter_button'
    # 【确定按钮】
    yesBtn = By.ID,'com.android.camera:id/done_button'
    # 【图片详情页选取按钮】
    selectBtn = By.ID,'com.huiian.timing:id/tv_crop_select'


    def click_backBtn(self):
        self.click(self.backBtn)
    def click_nextStep(self):
        self.click(self.nextStep)
    def click_choosePhoto(self):
        self.click(self.choosePhoto)
    def click_cameraBtn(self):
        self.click(self.cameraBtn)
    def click_shutterBtn(self):
        self.click(self.shutterBtn)
    def click_yesBtn(self):
        self.click(self.yesBtn)
    def click_selectBtn(self):
        self.click(self.selectBtn)

