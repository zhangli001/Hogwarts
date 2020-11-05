from appium.webdriver.common.mobileby import MobileBy

from app.app_wework.page.ContactDetailSetting_page import ContactDetailSetting_Page
from app.app_wework.page.base_page import BasePage


class ContactDetailBriefInfoProfile_Page(BasePage):
    # 进入到个人信息-设置页面
    def goto_ContactDetailSetting(self):
        # 在个人信息页面，点击右上角的按钮
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/guk")
        return ContactDetailSetting_Page(self.driver)

