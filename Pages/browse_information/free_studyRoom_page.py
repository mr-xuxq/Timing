#——————免费自习室首页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Free_studyRoom(BaseAction):
    # 【精准匹配按钮】
    matchFriendBtn = By.ID, 'com.huiian.timing:id/iv_main_action_match_friend'
    # 【关闭道友圈按钮】
    closeFriendCircleBtn = By.ID, 'com.huiian.timing:id/iv_close'
    # 【免费区按钮】
    freeArea = By.ID, 'com.huiian.timing:id/tv_free'
    # 【加入自习室按钮】
    joinFreeStudyRoom = By.ID, 'com.huiian.timing:id/btn_join_room'

    def click_matchFriendBtn(self):
        self.click(self.matchFriendBtn)
    def click_closeFriendCircleBtn(self):
        self.click(self.closeFriendCircleBtn)
    def click_freeArea(self):
        self.click(self.freeArea)
    def click_joinFreeStudyRoom(self):
        self.click(self.joinFreeStudyRoom)







