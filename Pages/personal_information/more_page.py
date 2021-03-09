#——————更多页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class More(BaseAction):
    # 【更多按钮】
    moreBtn = By.ID, 'com.huiian.timing:id/iv_main_more'
    # 【设置按钮】
    settingBtn = By.ID, 'com.huiian.timing:id/tv_setting'
    # 【更多按钮2】
    smallmoreBtn = By.ID, 'com.huiian.timing:id/tv_setting'
    # 更多_用户区域
    personBtn = By.ID, 'com.huiian.timing:id/iv_avatar'
    # 自律工具
    # 学习计时按钮
    normalTimingBtn = By.XPATH, '//*[@text="开始学习"]'
    # 视频打卡按钮
    videoBtn = By.XPATH, '//*[@text="视频打卡"]'
    # 番茄计时按钮
    tomatoBtn = By.ID, 'com.huiian.timing:id/tv_tomato_timing_common'
    # 学习农场按钮
    farmBtn = By.XPATH, '//*[@text="学习农场"]'

    # 起床睡觉按钮
    sleepBtn = By.XPATH, '//*[@text="起床睡觉"]'
    # 发布/投稿按钮
    postBtn = By.ID, 'com.huiian.timing:id/tv_publish'
    # 学习计划按钮
    planBtn = By.XPATH, '//*[@text="学习计划"]'
    # 学习群按钮
    groupBtn = By.XPATH, '//*[@text="学习群"]'
    # 图书馆按钮
    libraryBtn = By.XPATH, '//*[@text="图书馆"]'
    # 我的已购按钮
    shopBtn = By.XPATH, '//*[@text="我的已购"]'
    #【+创建学习群】按钮
    createGroup = By.ID,'com.huiian.timing:id/tv_create'
#-----------------------------------------------------------------------------
    #关注列表的人数
    followCount = By.ID,'com.huiian.timing:id/tv_follow_count'
    #粉丝列表人数
    fansCount = By.ID,'com.huiian.timing:id/tv_fans_count'
#------------------------------------------------------------------------------
    #身份认证按钮
    identificationBtn = By.ID,'com.huiian.timing:id/tv_identification'

    def click_more(self):
        self.click(self.moreBtn)
    def click_setting(self):
        self.click(self.settingBtn)
    def click_person(self):
        self.click(self.personBtn)
    def click_normalTiming(self):
        self.click(self.normalTimingBtn)
    def click_video(self):
        self.click(self.videoBtn)
    def click_sleep(self):
        self.click(self.sleepBtn)
    def click_tomato(self):
        self.click(self.tomatoBtn)
    def click_farm(self):
        self.click(self.farmBtn)
    def click_group(self):
        self.click(self.groupBtn)
    def click_createGroup(self):
        self.click(self.createGroup)
    def click_postBtn(self):
        self.click(self.postBtn)

    def swipeByMore(self):
        self.swipeOperat(0.5, 0.9, 0.5, 0.1, 500)
    #500 = 0.5S
    def swipeByTime(self):
        self.swipeOperat(0.6, 0.8, 0.6, 0.74, 500)

    #坐标点击睡觉
    def clickCoordinate_sleep(self):
        self.clickOperat(0.5, 0.84, 0.5, 0.87, 500)
        #self.clickOperat(0.5, 0.84, 0.5, 0.84, 500)
    # self.driver.tap([(520, 2037), (521, 2037)], 500)(1080*2340)
    #[329,1969][481,2013]

    #坐标点击起床
    def clickCoordinate_getUp(self):
        self.clickOperat(0.30,0.80,0.44,0.80,500)
    # self.driver.tap([(530, 1888), (531, 1889)], 500)(1080*2340)
    #[300, 1827][510, 2037]

    def waitAndfind_sleepBtn(self):
        if self.waitLoading(self.sleepBtn, t=2) == True:
            return True
        else:
            return False

    def waitAndfind_more(self):
        if self.waitLoading(self.moreBtn, t=2) == True:
            return True
        else:
            return False
# --------------------------------------------------------------------------
    def get_followCount(self):
        count = self.driver.find_element_by_id('com.huiian.timing:id/tv_follow_count').text
        return count
    def get_fansCount(self):
        count = self.driver.find_element_by_id('com.huiian.timing:id/tv_fans_count').text
        return count
    def click_followCount(self):
        self.driver.click(self.followCount)

    def swipeByRefresh(self):
        self.swipeOperat(0.5, 0.5, 0.5, 0.7, 500)
    def compare_count(self,x1,x2):
        if x1 == x2:
            return True
        else:
            return False

    # def getCountByResourceId(self):
    #     num = 0
    #     i = 0
    #     for i in [0,100]:
    #         self.driver.find_element_by_id('com.huiian.timing:id/tv_fans_count')
    #         i = i+1
    #     else:
    #         num = i
    #         break
    #     return  num
#--------------------------------------------------------------------------------------------------
    def click_identification(self):
        self.click(self.identificationBtn)

    def check_moreBtn(self):
        return self.is_feature_exist(self.moreBtn)

    #坐标点击起床
    def simpleTap(self,x,y):
        self.tapOperat(x,y)

    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,300)