#—————————-关注页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Follow(BaseAction):
    # 【关注页按钮】
    followBtn = By.ID, 'com.huiian.timing:id/follow_img'
    # 【删除日记按钮】
    taget = By.ID, 'com.huiian.timing:id/iv_del'


    def click_follow(self):
        self.click(self.followBtn)
    def click_deleteDiaryBtn(self):
        self.click(self.taget)


    def waitAndFind(self):
        if  self.waitLoading(self.taget,t=5) == True:
            return True
        else:
            return False


