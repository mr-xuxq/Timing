# import time, allure
# from Pages.page import Page
# from base.base_driver import Base
#
# @allure.feature('聊天页功能')
# class Test_friendChat():
#     def setup(self):
#         self.driver = Base().init_driver()
#         self.driver.implicitly_wait(50)
#         self.page = Page(self.driver)
#     def teardown(self):
#         self.driver.quit()
#
#     @allure.story('聊天页面红点')
#     def test_pointVanish(self):
#         with allure.step('进入消息页面'):
#             self.page.message().click_messageBtn()
#         with allure.step('滑动页面找红点，找到就点击进入再返回'):
#             i = 0
#             while i < 3:
#                 #如果消息页面channel红点存在
#                 if self.page.message().check_messagePoint() == True:
#                     #点击进入
#                     self.page.message().click_messagePoint()
#                     if self.page.friend_chat().check_groupMore() == True:
#                         with allure.step('如果红点类型是讨论组和打卡群时，点击进入成员动态页，再返回至消息页'):
#                             self.page.friend_chat().click_groupMore()
#                             self.page.friend_chat().click_groupActive()
#                             time.sleep(10)
#                             # 返回至消息页
#                             self.driver.press_keycode(4)
#                             self.driver.press_keycode(4)
#                             self.driver.press_keycode(4)
#                     elif self.page.friend_chat().check_groupChat() == True:
#                         with allure.step('如果红点类型是契约群时，点击进入聊天页，再返回至消息页'):
#                             self.page.friend_chat().click_groupActive()
#                             time.sleep(5)
#                             self.page.friend_chat().click_groupChat()
#                             time.sleep(5)
#                             self.driver.press_keycode(4)
#                     else:
#                         with allure.step('如果红点类型是道友聊天和学习数据时，点击进入，再返回至消息页'):
#                             self.driver.press_keycode(4)
#                 else:
#                     with allure.step('如果没有找到红点，上滑页面继续找红点'):
#                         self.page.message().swipeByMessage()
#                         i += 1
#         with allure.step('校验结果：如果页面还存在红点——>失败'):
#             assert self.page.message().waitAndfind_messagePoint() == False