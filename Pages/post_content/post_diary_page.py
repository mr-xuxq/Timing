#——————发布日记主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Post_diary(BaseAction):
    # 【发布按钮】
    postBtn = By.ID, 'com.huiian.timing:id/activity_banner_right_tv'
    # 【添加图片按钮】
    addPictureBtn = By.ID, 'com.huiian.timing:id/image_iv'
    # 【日记主题按钮】
    addTopicBtn = By.ID, 'com.huiian.timing:id/tv_topic'
    # 【日记内容编辑框】
    diaryContentBox = By.ID, 'com.huiian.timing:id/content_et'
    # 【退出按钮】
    closeBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_iv'
    #【确认退出_保存】
    closeSaveBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_right_fl'
    #【确认退出_不保存】
    closeNotSaveBtn = By.ID, 'com.huiian.timing:id/popupwindow_confirm_left_fl'


    def click_post(self):
        self.click(self.postBtn)

    def click_addPictureBtn(self):
        self.click(self.addPictureBtn)

    def click_addTopicBtn(self):
        self.click(self.addTopicBtn)

    def input_diaryContent(self, content):
        self.input(self.diaryContentBox,content)

    def click_close(self):
        self.click(self.closeBtn)

    def click_closeSave(self):
        self.click(self.closeSaveBtn)

    def click_closeNotSave(self):
        self.click(self.closeNotSaveBtn)


