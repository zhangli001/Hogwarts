from appium.webdriver.common.mobileby import MobileBy

from app.app_wework.page.ContactEdit_page import ContactEdit_Page
from app.app_wework.page.base_page import BasePage


class ContactDetailSetting_Page(BasePage):
    def goto_ContactEdit(self):
        # 点击“编辑成员”按钮
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/azd")
        return ContactEdit_Page(self.driver)

    # 进入到编辑页面
