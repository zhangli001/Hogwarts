import pytest

from app.app_wework.page.app import App


class TestContact:
    global name
    name = "zltest90"

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    @pytest.mark.run(order=1)
    def test_addcontact(self):
        gender = "男"
        phonenum = "135000000409"
        result = self.main.goto_address() \
            .click_addmember().add_member_menual() \
            .add_contract(name, gender, phonenum).get_toast()
        assert result == '添加成功'

    @pytest.mark.run(order=2)
    def test_deletecontract(self):
        self.main.goto_address()\
            .click_member(name).\
            goto_ContactDetailSetting()\
            .goto_ContactEdit().delete_contact()
        # 验证是否删除成功
        all_elements = self.main.driver.page_source
        assert name not in all_elements
