#——————发布日记的选择照片页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Select_diary_photo(BaseAction):
    # 【照片选择按钮_默认选择第一张】
    selectPhotoBtn =By.ID,'com.huiian.timing:id/check_view'
    # 【照片选择_下一步按钮】
    nextBtn =By.ID,'com.huiian.timing:id/tv_next'

    # 【照片编辑_下一步按钮】
    selectedBtn =By.ID,'com.huiian.timing:id/btn_next'
    # 【照片选择_后退按钮】
    backToSelectBtn =By.ID,'com.huiian.timing:id/iv_back'

    def click_selectPhotoBtn(self):
        self.click(self.selectPhotoBtn)
    def click_nextBtn(self):
        self.click(self.nextBtn)
    def click_selected(self):
        self.click(self.selectedBtn)
    def click_backToSelect(self):
        self.click(self.backToSelectBtn)