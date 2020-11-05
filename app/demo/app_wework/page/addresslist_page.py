# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.app_wework.page.ContactDetailBriefInfoProfile_page import ContactDetailBriefInfoProfile_Page
from app.app_wework.page.base_page import BasePage
from app.app_wework.page.memberinvitemenu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_addmember(self):
        # self.find(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def click_member(self, name):
        self.find_by_scroll(name).click()
        return ContactDetailBriefInfoProfile_Page(self.driver)

    def get_member_number(self):
        pass
