#——————发布日记的选择封面页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Select_cover(BaseAction):
    # 【完成按钮】
    nextBtn =By.ID,'com.huiian.timing:id/tv_confirm'

    def click_next(self):
        self.click(self.nextBtn)
