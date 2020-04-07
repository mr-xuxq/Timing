#——————修改姓名页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Name_info(BaseAction):
    #姓名输入框
    nameBox = By.ID,'com.huiian.timing:id/name_et'
    #姓名页面_确定按钮
    nameRightBtn = By.XPATH,'//*[@text="确定"]'

    def click_nameRight(self):
        self.click(self.nameRightBtn)
    def input_nameBox(self,context):
        self.input(self.nameBox,context)
