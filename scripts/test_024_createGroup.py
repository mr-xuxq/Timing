import time, allure
from base.base_driver import Base
from Pages.page import Page

@allure.feature('创建学习群功能')
class Test_createGroup():
    def setup(self):
        self.driver = Base().init_driver()
        # 设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.story('创建讨论组')
    def test_discussTeam(self):
        with allure.step('进入更多页面'):
            self.page.more().click_more()
            time.sleep(5)
        with allure.step('点击【+】学习群'):
            self.page.shouye().click_post()
            self.page.more().click_createGroup()
        with allure.step('选择创建学习讨论小组'):
            self.page.create_group().click_discussTeam()
            self.page.create_group().click_nextStep()
            self.page.create_group().click_chooseFriend()
            self.page.create_group().click_chooseFriendDo()
            assert self.page.create_group().waitAndfind_createdDiscussTeam() == True

#账号条件：  粉丝50
    # @allure.story('创建打卡群')
    # def test_recordTeam(self):
    #     with allure.step('进入更多页面'):
    #         self.page.more().click_more()
    #         time.sleep(5)
    #     with allure.step('滑动更多页面至底部'):
    #         self.page.more().swipeByMore()
    #     with allure.step('点击学习群'):
    #         time.sleep(1)
    #         self.page.more().click_group()
    #     with allure.step('选择创建打卡群'):
    #         self.page.create_group().click_recordTeam()
    #         self.page.create_group().click_nextStep()
    #         self.page.create_group().click_choiceGroupPhoto()
    #         # 在选择照片页选择第一张照片
    #         self.driver.tap([(361, 220), (719, 578)], 500)
    #         # 保存修改的头像
    #         self.page.choose_image().click_imgSummit()
    #         self.page.create_group().input_tearmName('A recordTeam')
    #         self.page.create_group().input_introTeam('A intro')
    #         self.page.create_group().click_nextStep()
    #         self.page.create_group().click_recordTeamSuccess()
    #         assert self.page.create_group().waitAndfind_createdDiscussTeam() == True