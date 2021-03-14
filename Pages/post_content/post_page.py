#——————发布主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Post(BaseAction):
    # 【发布/投稿】
    postDiary = By.XPATH, '//*[@text="发布/投稿"]'
    # 【发布图文日记】
    postPhotoDiary = By.ID, 'com.huiian.timing:id/tv_post_diary'
    # 【发布视频日记】
    postVideoDiary = By.ID, 'com.huiian.timing:id/tv_post_video_diary'
    # 【投稿汤视频】
    postsVlog = By.ID, 'com.huiian.timing:id/tv_post_vlog'
    # 【我的草稿箱】
    drafts = By.ID, 'com.huiian.timing:id/tv_my_drafts'
    # 【后退按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_back'

    def click_postDiary(self):
        self.click(self.postDiary)
    def click_postPhotoDiary(self):
        self.click(self.postPhotoDiary)
    def click_postVideoDiary(self):
        self.click(self.postVideoDiary)
    def click_postsVlog(self):
        self.click(self.postsVlog)
    def click_drafts(self):
        self.click(self.drafts)
    def click_close(self):
        self.click(self.closeBtn)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)

