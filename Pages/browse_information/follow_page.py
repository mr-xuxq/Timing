#—————————-关注页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Follow(BaseAction):
    # 【删除日记按钮】
    deleteDiaryBtn = By.ID, 'com.huiian.timing:id/iv_del'
    # 【确认删除日记按钮】
    yesBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'
    # 【发布成功弹窗】
    postSuccess = By.XPATH, '//*[@text="日记发布成功"]'
    # 【发布按钮】
    postBtn = By.ID, 'com.huiian.timing:id/iv_post'
    # 【发布视频按钮】
    postVideoDiaryBtn = By.ID, 'com.huiian.timing:id/iv_post_video_diary'
    # 【发布图文按钮】
    postPhotoDiaryBtn = By.ID, 'com.huiian.timing:id/iv_post_diary'
    # 【关闭发布按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/iv_post_close'
    # 【精准匹配按钮】
    matchFriendBtn = By.ID, 'com.huiian.timing:id/iv_main_action_match_friend'
    # 【关闭道友圈按钮】
    closeFriendCircleBtn = By.ID, 'com.huiian.timing:id/iv_close'

    def click_deleteDiaryBtn(self):
        self.click(self.deleteDiaryBtn)
    def click_yesBtn(self):
        self.click(self.yesBtn)
    def click_postBtn(self):
        self.click(self.postBtn)
    def click_postVideoDiaryBtn(self):
        self.click(self.postVideoDiaryBtn)
    def click_postPhotoDiaryBtn(self):
        self.click(self.postPhotoDiaryBtn)
    def click_closeBtn(self):
        self.click(self.closeBtn)
    def click_matchFriendBtn(self):
        self.click(self.matchFriendBtn)
    def click_closeFriendCircleBtn(self):
        self.click(self.closeFriendCircleBtn)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def check_postSuccess(self):
        return self.is_feature_exist(self.postSuccess)
    def check_deleteDiaryBtn(self):
        return self.is_feature_exist(self.deleteDiaryBtn)



