#——————发布主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Post_content(BaseAction):
    # 【发布按钮】
    postBtn = By.ID, 'com.huiian.timing:id/ll_post'
    # 【发布图文日记按钮】
    postDiaryBtn = By.ID, 'com.huiian.timing:id/cl_post_diary'
    # 【上传长视频按钮】
    postVideoBtn = By.ID, 'com.huiian.timing:id/cl_post_video'
    # 【学习计时按钮】
    normalTimingBtn = By.ID, 'com.huiian.timing:id/cl_study_timing'
    # 【起床睡觉按钮】
    sleepBtn = By.ID, 'com.huiian.timing:id/cl_wake_sleep'
    # 【视频打卡按钮】
    videoRecordBtn = By.ID, 'com.huiian.timing:id/cl_video_dk'
    # 【图书馆按钮】
    libraryBtn = By.ID, 'com.huiian.timing:id/cl_library'
    # 【创建学习群按钮】
    createGroupBtn = By.ID, 'com.huiian.timing:id/cl_create_group'
    # 【关闭按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_back'

    def click_post(self):
        self.click(self.postBtn)

    def click_postDiary(self):
        self.click(self.postDiaryBtn)

    def click_postVideo(self):
        self.click(self.postVideoBtn)

    def click_normalTiming(self):
        self.click(self.normalTimingBtn)

    def click_sleep(self):
        self.click(self.sleepBtn)

    def click_videoRecord(self):
        self.click(self.videoRecordBtn)

    def click_library(self):
        self.click(self.libraryBtn)

    def click_createGroup(self):
        self.click(self.createGroupBtn)

    def click_close(self):
        self.click(self.closeBtn)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)

