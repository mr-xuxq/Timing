#——————修改姓名页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NameInfo(BaseAction):
    #姓名输入框
    nameBox = By.ID,'com.huiian.timing:id/name_et'
    #姓名页面_确定按钮
    namedoBtn = By.XPATH,'//*[@text="确定"]'


    def click_nameInfo(self,target):
        self.click(target)
    def input_nameContext(self,target, text):
        self.input(target,text)

    def swipeByMy(self,x1, y1, x2, y2, t):
        self.swipeOperat(x1, y1, x2, y2, t)

    def waitAndfind(self, target, t):
        if self.waitLoading(target, t) == True:
            return True
        else:
            return False