#——————发布长视频主页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Post_video(BaseAction):
    # 【发布按钮】
    postBtn = By.ID, 'com.huiian.timing:id/tv_post_vlog'
    # 【参与话题栏】
    addTopicBtn = By.ID, 'com.huiian.timing:id/tv_topic'
    # 【编辑标题栏】
    addTitleBox = By.ID, 'com.huiian.timing:id/et_content'


    def click_post(self):
        self.click(self.postBtn)

    def click_addTopicBtn(self):
        self.click(self.addTopicBtn)

    def input_addTitleBox(self, content):
        self.input(self.addTitleBox,content)



