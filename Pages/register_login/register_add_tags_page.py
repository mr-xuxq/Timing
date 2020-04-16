#——————注册的添加标签页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Register_add_tags(BaseAction):
    # 自定义标签按钮
    customLabelBtn =By.ID,'com.huiian.timing:id/tv_go_custom'
    # 【英语标签按钮】
    labelBtn =By.XPATH,'//*[@text="英语"]'
    # 【下一步按钮】
    nextBtn =By.ID,'com.huiian.timing:id/tv_next'


    def click_labelBtn(self):
        self.click(self.labelBtn)

    def click_nextBtn(self):
        self.click(self.nextBtn)

