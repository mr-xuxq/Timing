#——————发布日记的选择视频页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Select_diary_video(BaseAction):

    # 【照片选择按钮_默认选择第一张】
    selectVideoBtn =By.ID,'com.huiian.timing:id/tv_num'
    # 【照片选择_下一步按钮】
    nextBtn =By.ID,'com.huiian.timing:id/tv_next'




    def click_selectVideoBtn(self):
        self.click(self.selectVideoBtn)
    def click_nextBtn(self):
        self.click(self.nextBtn)

