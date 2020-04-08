import time, allure
from Pages.page import Page
from base.base_driver import Base
from Pages.personal_information.more_page import More
from Pages.personal_information.person_home_page import Person_home
from Pages.personal_information.editPersonInfo_page import Edit_personal_info
from Pages.personal_information.nameInfo_page import Name_info
from Pages.message_interaction.chat_chooseImage_page import Choose_image

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
            self.page.more().click_more(More.moreBtn)
            time.sleep(3)
        with allure.step('进入个人主页'):
            self.page.more().click_more(More.personBtn)
        with allure.step('进入修改资料页'):
            self.page.person_home().click_person(Person_home.personInfo)
        with allure.step('进入修改姓名页，输入新昵称并保存'):
            self.page.edit_personal_info().click_personInfo(Edit_personal_info.nameBtn)
            #输入修改后的姓名
            self.page.name_info().input_nameContext(Name_info.nameBox,'new name')
            #保存修改后的姓名
            self.page.name_info().click_nameInfo(Name_info.namedoBtn)
        with allure.step('校验结果：新昵称保存成功——>成功'):
            assert self.page.edit_personal_info().waitAndfind(Edit_personal_info.nameNew, 1) == True

    # # 修改性别
    # def test_sexInfo(self):
    #     #进入更多页面
    #     self.page.more().click_more(More.moreBtn)
    #     time.sleep(3)
    #     #进入个人主页
    #     self.page.more().click_more(More.personBtn)
    #     #进入修改资料页
    #     self.page.person().click_person(Person.personInfo)
    #     #修改性别栏
    #     self.page.personInfo().click_personInfo(PersonInfo.genderBtn)
    #     #滑动选择性别
    #     self.page.personInfo().swipeByMy(0.6, 0.8, 0.6, 0.75, 150)
    #     #提交修改后的性别选择
    #     self.page.personInfo().click_personInfo(PersonInfo.genderSubmit)
    #     assert self.page.personInfo().waitAndfind(PersonInfo.???, 1) == True

    @allure.story('修改头像信息')
    def test_imgInfo(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more(More.moreBtn)
            time.sleep(3)
        with allure.step('进入个人主页'):
            self.page.more().click_more(More.personBtn)
        with allure.step('进入修改资料页'):
            self.page.person_home().click_person(Person_home.personInfo)
        with allure.step('进入选择照片页'):
            #点击头像进入选择照片页
            self.page.edit_personal_info().click_personInfo(Edit_personal_info.myimgBtn)
        with allure.step('在选择照片页选择第一张照片，并保存'):
            #在选择照片页选择第一张照片
            self.driver.tap([(361,220),(719,578)], 500)
            #保存修改的头像
            self.page.choose_image().click_chooseImage(Choose_image.imgSummit)
            self.page.edit_personal_info().click_personInfo(Edit_personal_info.infoSubmit)
        with allure.step('校验结果：头像保存成功——>成功'):
            assert self.page.person_home().waitAndfind(Person_home.personInfo, 1) == True




