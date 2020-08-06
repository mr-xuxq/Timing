#——————长视频列表页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class List_sVlog(BaseAction):
    # 【后退按钮】
    backBtn = By.ID, 'com.huiian.timing:id/iv_back'
    # 【目标-sVlog标题】
    sVlogTitle = By.ID, 'com.huiian.timing:id/tv_content_vloglist'
<<<<<<< HEAD

=======
    # 【推荐】按钮
    recommendBtn = By.XPATH, '//*[@text="推荐"]'
>>>>>>> 78ef5ac86c52608068f40fecb91b0e3097a77cf2

    def click_back(self):
        self.click(self.backBtn)

    def click_recommend(self):
        self.click(self.recommendBtn)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,150)
<<<<<<< HEAD

=======

    def swipeDown(self):
        self.swipeOperat(0.5, 0.2, 0.5, 0.8, 150)

    def swipeLeft(self):
        self.swipeOperat(0.8, 0.8, 0.2, 0.8, 150)

>>>>>>> 78ef5ac86c52608068f40fecb91b0e3097a77cf2
    def check_sVlogTitle(self):
        return self.is_feature_exist(self.sVlogTitle)