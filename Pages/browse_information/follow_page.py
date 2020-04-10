#—————————-关注页—————-—-——#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Follow(BaseAction):
    # 【关注页按钮】
    followBtn = By.ID, 'com.huiian.timing:id/follow_img'
    # 【删除日记按钮】
    deleteDiaryBtn = By.ID, 'com.huiian.timing:id/iv_del'
    # 【确认删除日记按钮】
    yesBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'
    # 【删除成功弹窗】
    postSuccess = By.XPATH, '//*[@text="日记发布成功"]'
    # 【删除成功弹窗】
    deleteSuccess = By.XPATH, '//*[@text="34567890JQKA2"]'

    def click_follow(self):
        self.click(self.followBtn)
    def click_deleteDiaryBtn(self):
        self.click(self.deleteDiaryBtn)
    def click_yesBtn(self):
        self.click(self.yesBtn)
    def check_deleteDiaryBtn(self):
        return self.is_feature_exist(self.deleteDiaryBtn[1])
    def check_postSuccess(self):
        return self.is_feature_exist(self.postSuccess[1])
    def check_deleteSuccess(self):
        return self.is_feature_exist(self.deleteSuccess[1])


