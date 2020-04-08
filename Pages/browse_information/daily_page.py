#—————————-日记详情页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Daily(BaseAction):
    # 日记详情页_+关注按钮
    followBtn = By.ID, 'com.huiian.timing:id/tv_follow_view'

    def click_followBtn(self):
        self.click(self.followBtn)
