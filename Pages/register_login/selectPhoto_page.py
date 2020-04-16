#——————注册的选择照片页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Select_photo(BaseAction):
    # 照片选择按钮
    photoBtn =By.ID,'com.huiian.timing:id/photo_list_item_img'
    # 照片详情【选取按钮】
    selectBtn = By.ID,'com.huiian.timing:id/tv_crop_select'


    def click_photoBtn(self):
        self.click(self.photoBtn)
    def click_selectBtn(self):
        self.click(self.selectBtn)
