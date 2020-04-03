#——————个人主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Person(BaseAction):
    #修改资料按钮
    personInfo = By.XPATH,'//*[@text="修改资料"]'

    def click_person(self,target):
        self.click(target)
    #上滑更多页面至计时区域
    def swipeByMy(self,x1, y1, x2, y2, t):
        self.swipeOperat(x1, y1, x2, y2, t)

    def input_ContentBox(self,target,content):
        self.input(target,content)

    def waitAndfind(self, target, t):
        if self.waitLoading(target, t) == True:
            return True
        else:
            return False