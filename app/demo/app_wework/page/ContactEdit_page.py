from appium.webdriver.common.mobileby import MobileBy

from app.app_wework.page.base_page import BasePage


class ContactEdit_Page(BasePage):
    def delete_contact(self):
        # 点击“删除”按钮
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/duq")

        # 在“删除成员”提示框，点击“确定”按钮
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/b_4")
