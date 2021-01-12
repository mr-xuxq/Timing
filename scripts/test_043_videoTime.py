# #coding:utf-8
# from Pages.page import Page
# from base.base_driver import Base
# import allure,time
#
#
# class Test_videoTime():
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
#     def test_videoTimeLess(self):
#         with allure.step('视频打卡计时不足一分钟结束'):
#             with allure.step('更多页滑到底部'):
#                 self.page.more().click_more()
#                 time.sleep(3)
#                 self.page.more().swipeByMore()
#             with allure.step('点击视频打卡'):
#                 time.sleep(3)
#                 self.page.more().tapOperat(0.387, 0.15)
#             with allure.step('填写学习内容'):
#                 self.page.timing().input_videoContentBox(12345)
#             with allure.step('设置时间'):
#                 self.page.timing().click_videoSettingBtn()
#             with allure.step('设置学习时长'):
#                 time.sleep(3)
#                 self.page.more().swipeByTime()
#             with allure.step('点击设置完成按钮'):
#                 self.page.timing().click_studySettingsuccessBtn()
#             with allure.step('点击确定开启并开启摄像头'):
#                 self.page.timing().click_startVideoBtn()
#             with allure.step('判断是否有录视频权限弹窗'):
#                 result = self.page.timing().check_videoStartDialog()
#                 if result == True :
#                     with allure.step('打开权限'):
#                         self.page.timing().click_videoStartDialog()
#                 else:
#                     pass
#             with allure.step('点击开始学习按钮'):
#                 self.page.timing().click_videoStartStudy()
#             with allure.step('点击结束'):
#                 time.sleep(3)
#                 self.page.timing().click_timingEnd()
#             with allure.step('点击确定'):
#                 self.page.timing().click_videoEndDialog()
#             with allure.step('判断到了更多页'):
#                 assert self.page.more().waitAndfind_more() == True
#
#     def test_videoTimeEnough(self):
#         with allure.step('视频打卡足够一分钟后点击结束'):
#             with allure.step('更多页滑到底部'):
#                 self.page.more().click_more()
#                 time.sleep(3)
#                 self.page.more().swipeByMore()
#             with allure.step('点击视频打卡'):
#                 time.sleep(3)
#                 self.page.more().tapOperat(0.387, 0.15)
#             with allure.step('填写学习内容'):
#                 self.page.timing().input_videoContentBox(12345)
#             with allure.step('设置时间'):
#                 self.page.timing().click_videoSettingBtn()
#             with allure.step('设置学习时长'):
#                 time.sleep(3)
#                 self.page.more().swipeByTime()
#             with allure.step('点击设置完成按钮'):
#                 self.page.timing().click_studySettingsuccessBtn()
#             with allure.step('点击确定开启并开启摄像头'):
#                 self.page.timing().click_startVideoBtn()
#             with allure.step('判断是否有录视频权限弹窗'):
#                 result = self.page.timing().check_videoStartDialog()
#                 if result == True:
#                     with allure.step('打开权限'):
#                         self.page.timing().click_videoStartDialog()
#                 else:
#                     pass
#             with allure.step('点击开始学习按钮'):
#                 self.page.timing().click_videoStartStudy()
#             with allure.step('判断时间到了结束弹窗'):
#                 time.sleep(50)
#                 assert self.page.timing().check_timingDialog() == True
#             with allure.step('点击我知道了'):
#                 self.page.timing().click_timingDialog()
#             with allure.step('点击结束'):
#                 self.page.timing().click_timingEnd()
#             with allure.step('点击确定'):
#                 self.page.timing().click_videoEndDialog()
#             with allure.step('判断到了视频打卡页面'):
#                 assert self.page.timing().waitAndfind_videoSuccess()==True
#             with allure.step('点击关闭按钮'):
#                 self.page.timing().click_videoClosBtn()
#             with allure.step('判断到了完成页面'):
#                 assert self.page.timing().waitAndfind_timingEndSuccess()==True
#
