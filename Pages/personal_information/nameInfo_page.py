#——————修改姓名页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Name_info(BaseAction):
    #姓名输入框
    nameBox = By.ID,'com.huiian.timing:id/et_name'
    #保存按钮
    nameRightBtn = By.ID,'com.huiian.timing:id/activity_banner_right_tv'

    def click_nameRight(self):
        self.click(self.nameRightBtn)
    def input_nameBox(self,context):
        self.input(self.nameBox,context)
