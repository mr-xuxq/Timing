#——————更多页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class More(BaseAction):
    # 【更多按钮】
    moreBtn = By.ID, 'com.huiian.timing:id/mine_img'
    # 【设置按钮】
    settingBtn = By.ID, 'com.huiian.timing:id/iv_setting'
    # 更多_用户区域
    personBtn = By.ID, 'com.huiian.timing:id/view_info'
    # 学习计时按钮
    timingBtn = By.XPATH, '//*[@text="学习计时"]'
    # 视频打卡按钮
    videoBtn = By.XPATH, '//*[@text="视频打卡"]'
    # 起床睡觉按钮
    sleepBtn = By.XPATH, '//*[@text="起床睡觉"]'
    # 番茄计时按钮
    tomatoBtn = By.ID, 'com.huiian.timing:id/tv_tomato_timing_common'
    # 学习农场按钮
    farmBtn = By.XPATH, '//*[@text="学习农场"]'
    # 学习计划按钮
    planBtn = By.XPATH, '//*[@text="学习计划"]'
    # 学习群按钮
    groupBtn = By.XPATH, '//*[@text="学习群"]'
    # 图书馆按钮
    libraryBtn = By.XPATH, '//*[@text="图书馆"]'
    # 我的已购按钮
    shopBtn = By.XPATH, '//*[@text="我的已购"]'

    def click_more(self):
        self.click(self.moreBtn)

    def click_setting(self):
        self.click(self.settingBtn)

    def click_person(self):
        self.click(self.personBtn)

    def click_timing(self):
        self.click(self.timingBtn)

    def click_video(self):
        self.click(self.videoBtn)

    def click_sleep(self):
        self.click(self.sleepBtn)

    def click_tomato(self):
        self.click(self.tomatoBtn)

    def click_farm(self):
        self.click(self.farmBtn)

    def click_plan(self):
        self.click(self.planBtn)

    def click_groupBtn(self):
        self.click(self.groupBtn)

    def click_plibrary(self):
        self.click(self.libraryBtn)

    def click_shop(self):
        self.click(self.shopBtn)

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