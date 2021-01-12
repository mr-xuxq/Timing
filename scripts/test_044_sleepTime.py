# #coding:utf-8
# from Pages.page import Page
# from base.base_driver import Base
# import allure,time
#
#
# class Test_sleepTime():
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
#     def test_sleepTime(self):
#         with allure.step('更多页滑动到最底部'):
#             self.page.more().click_more()
#             time.sleep(3)
#             self.page.more().swipeByMore()
#         with allure.step('点击起床睡觉'):
#             time.sleep(3)
#             self.page.more().tapOperat(0.614, 0.148)
#         with allure.step('点击睡觉'):
#             time.sleep(3)
#             self.page.more().tapOperat(0.505, 0.838)
#         with allure.step('关闭打卡弹窗'):
#             time.sleep(3)
#             self.page.timing().click_sleepingClose()
#             time.sleep(3)
#         with allure.step('点击起床按钮'):
#             self.page.timing().click_sleepingWake()
#         with allure.step('判断睡觉计时结束'):
#             assert self.page.timing().check_sleepingClose()== True