#coding:utf-8
import time,allure
from Pages.page import Page
from base.base_driver import Base

class Test_postDiary():
    def setup(self):
        self.driver = Base().init_driver()
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    #判断元素是否在当前页面内
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    #长视频列表页浏览测试用例
    def test_postDiary(self):
        with allure.step('进入发布页'):
            self.page.shouye().click_post()
        with allure.step('点击发布学习日记'):
            self.page.post_content().click_postDiary()
        with allure.step('点击上传图片'):
            self.page.post_diary().click_addPictureBtn()
        with allure.step('选定图片'):
            self.page.select_diary_photo().click_selectPhotoBtn()
        with allure.step('下一步，进入图片编辑页'):
            self.page.select_diary_photo().click_nextBtn()
        with allure.step('已确定图片，进入下一步'):
            self.page.select_diary_photo().click_selected()
        with allure.step('点击添加话题'):
            self.page.post_diary().click_addTopicBtn()
        with allure.step('输入话题'):
            self.page.topic().input_topic("12345")
        with allure.step('完成话题编辑'):
            self.page.topic().click_next()
        with allure.step('输入日记正文'):
            self.page.post_diary().input_diaryContent("34567890JQKA2")
        with allure.step('点击发布按钮'):
            self.page.post_diary().click_post()
        # with allure.step('完成封面选择'):
        #     self.page.select_cover().click_next()
            time.sleep(10)
        # with allure.step('刷新关注页'):
        #     self.page.follow().click_follow()
        #     time.sleep(2)

        with allure.step('断言:日记发布成功'):
            assert self.page.follow().waitAndFind() == True
