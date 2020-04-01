from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class VideoRoom_list(BaseAction):
    # 【加入按钮】
    joinBtn = By.ID, 'com.huiian.timing:id/btn_join_room'

    def check_join(self):
        result = self.find_element(self.joinBtn,timeout=2, poll=1)
        if result == "":
            pass
        else:
            self.click(self.joinBtn)







