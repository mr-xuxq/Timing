#——————个人主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Person_home(BaseAction):
    #修改资料按钮
    personInfo = By.XPATH,'//*[@text="修改资料"]'

    def click_personInfo(self):
        self.click(self.personInfo)

    def waitAndfind_personInfo(self):
        if self.waitLoading(self.personInfo, t = 1) == True:
            return True
        else:
            return False