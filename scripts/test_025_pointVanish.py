import time, allure
# from Pages.page import Page
# from base.base_driver import Base
#
# @allure.feature('聊天页功能')
# class Test_friendChat():
#
#     #setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
#     #放一些准备的工作，或者准备一些测试数据。
#     def setup(self):
#         self.driver = Base().init_driver()
#         #设定全局等待
#         self.driver.implicitly_wait(50)
#         self.page = Page(self.driver)
#
#     #tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
#     #当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
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