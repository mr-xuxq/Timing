<<<<<<< HEAD
import time, allure,random
from Pages.page import Page
from base.base_driver import Base

@allure.feature('修改个人资料功能，前提：非认证账号')
class Test_changePersonalInformation():

    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('选择昵称进行修改')
    def test_nameInfo(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('进入个人主页'):
            self.page.more().click_person()
        with allure.step('进入修改资料页'):
            self.page.person_home().click_personInfo()
        with allure.step('进入修改姓名页，输入新昵称并保存'):
            self.page.edit_personal_info().click_name()
            #输入修改后的姓名
            name = random.randint(1, 10000)
            self.page.name_info().input_nameBox(name)
            #保存修改后的姓名
            time.sleep(5)
            self.page.name_info().click_nameRight()
        with allure.step('点击保存'):
            self.page.edit_personal_info().click_infoSubmit()
        with allure.step('校验结果：新昵称保存成功——>成功'):
            assert self.page.person_home().waitAndfind_personInfo() == True

    @allure.story('修改性别信息')
    def test_genderInfo(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('进入个人主页'):
            self.page.more().click_person()
        with allure.step('进入修改资料页'):
            self.page.person_home().click_personInfo()
        with allure.step('修改性别栏'):
            self.page.edit_personal_info().click_gender()
            time.sleep(2)
        with allure.step('滑动选择性别'):
            self.page.edit_personal_info().swipeByGender()
            time.sleep(2)
        with allure.step('提交修改后的性别选择'):
            self.page.edit_personal_info().click_genderSubmit()
            time.sleep(2)
        with allure.step('点击保存'):
            self.page.edit_personal_info().click_infoSubmit()
        with allure.step('校验结果：性别保存成功——>成功'):
            assert self.page.person_home().waitAndfind_personInfo() == True

    @allure.story('修改头像信息')
    def test_imgInfo(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(3)
        with allure.step('进入个人主页'):
            self.page.more().click_person()
        with allure.step('进入修改资料页'):
            self.page.person_home().click_personInfo()
        with allure.step('进入选择照片页'):
            #点击头像进入选择照片页
            self.page.edit_personal_info().click_myimg()
        with allure.step('在选择照片页选择第一张照片，并保存'):
            #在选择照片页选择第一张照片
            self.driver.tap([(361,220),(719,578)], 500)
            #保存修改的头像
            self.page.choose_image().click_imgSummit()
        with allure.step('点击保存'):
            self.page.edit_personal_info().click_infoSubmit()
        with allure.step('校验结果：头像保存成功——>成功'):
            assert self.page.person_home().waitAndfind_personInfo() == True





=======
# import time, allure,random
# from Pages.page import Page
# from base.base_driver import Base
#
# @allure.feature('修改个人资料功能，前提：非认证账号')
# class Test_changePersonalInformation():
#
#     def setup(self):
#         self.driver = Base().init_driver()
#         # 设定全局等待
#         self.driver.implicitly_wait(50)
#         self.page = Page(self.driver)
#
#     def teardown(self):
#         self.driver.quit()
#
#     @allure.story('选择昵称进行修改')
#     def test_nameInfo(self):
#         with allure.step('进入更多页面'):
#             self.page.more().click_more()
#             time.sleep(3)
#         with allure.step('进入个人主页'):
#             self.page.more().click_person()
#         with allure.step('进入修改资料页'):
#             self.page.person_home().click_personInfo()
#         with allure.step('进入修改姓名页，输入新昵称并保存'):
#             self.page.edit_personal_info().click_name()
#             #输入修改后的姓名
#             name = random.randint(1, 10000)
#             self.page.name_info().input_nameBox(name)
#             #保存修改后的姓名
#             time.sleep(5)
#             self.page.name_info().click_nameRight()
#         with allure.step('点击保存'):
#             self.page.edit_personal_info().click_infoSubmit()
#         with allure.step('校验结果：新昵称保存成功——>成功'):
#             assert self.page.person_home().waitAndfind_personInfo() == True
#
#     @allure.story('修改性别信息')
#     def test_genderInfo(self):
#         with allure.step('进入更多页面'):
#             self.page.more().click_more()
#             time.sleep(3)
#         with allure.step('进入个人主页'):
#             self.page.more().click_person()
#         with allure.step('进入修改资料页'):
#             self.page.person_home().click_personInfo()
#         with allure.step('修改性别栏'):
#             self.page.edit_personal_info().click_gender()
#             time.sleep(2)
#         with allure.step('滑动选择性别'):
#             self.page.edit_personal_info().swipeByGender()
#             time.sleep(2)
#         with allure.step('提交修改后的性别选择'):
#             self.page.edit_personal_info().click_genderSubmit()
#             time.sleep(2)
#         with allure.step('点击保存'):
#             self.page.edit_personal_info().click_infoSubmit()
#         with allure.step('校验结果：性别保存成功——>成功'):
#             assert self.page.person_home().waitAndfind_personInfo() == True
#
#     @allure.story('修改头像信息')
#     def test_imgInfo(self):
#         with allure.step('进入更多页面'):
#             self.page.more().click_more()
#             time.sleep(3)
#         with allure.step('进入个人主页'):
#             self.page.more().click_person()
#         with allure.step('进入修改资料页'):
#             self.page.person_home().click_personInfo()
#         with allure.step('进入选择照片页'):
#             #点击头像进入选择照片页
#             self.page.edit_personal_info().click_myimg()
#         with allure.step('在选择照片页选择第一张照片，并保存'):
#             #在选择照片页选择第一张照片
#             self.driver.tap([(361,220),(719,578)], 500)
#             #保存修改的头像
#             self.page.choose_image().click_imgSummit()
#         with allure.step('点击保存'):
#             self.page.edit_personal_info().click_infoSubmit()
#         with allure.step('校验结果：头像保存成功——>成功'):
#             assert self.page.person_home().waitAndfind_personInfo() == True
#
#
#
#
#
>>>>>>> 78ef5ac86c52608068f40fecb91b0e3097a77cf2
