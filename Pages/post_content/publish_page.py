#——————发布主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Post_content(BaseAction):
    # 发布按钮
    postBtn = By.ID, 'com.huiian.timing:id/learning_home_img'
    def click_main(self,target):
        self.click(target)

    def waitAndfind(self,target,t):
        if self.waitLoading(target,t) == True:
            return True
        else:
            return False

    def swipeByMy(self,x1, y1, x2, y2, t):
        self.swipeOperat(x1, y1, x2, y2, t)

