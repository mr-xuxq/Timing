#——————连麦房间列表页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Video_room_list(BaseAction):
    # 【加入按钮】
    joinBtn = By.ID, 'com.huiian.timing:id/btn_join_room'


    def click_joinBtn(self):
        self.click(self.joinBtn)

    def check_join(self):
        return  self.find_element(self.joinBtn,timeout=2, poll=1)
        # if result == "":
        #     pass
        # else:
        #     self.click(self.joinBtn)







