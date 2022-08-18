import os
import time
import pytest
from pages.pages_list import AuthPage, ResponsiblePage

main_link = 'https://test.dkrs.itmegastar.com/#/responsible-list'


def archive_fail(message, fio):
    print('\n>> ERROR!: Failed archiving the responsible.')
    print(f'>> Reason: {message}')
    print(f'>> Archive the responsible with this FIO: {fio}')


@pytest.mark.responsible
@pytest.mark.responsible_basis
class TestResponsibleBasis:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, main_link)
        page.open()
        page.should_be_auth_page()
        login = os.getenv('DKRS_ADMIN_LOGIN')
        password = os.getenv('DKRS_ADMIN_PASSWORD')
        page.auth(login, password)

        self.page = ResponsiblePage(browser, main_link)

    def test_can_see_performer_add_button(self, browser):
        self.page.should_be_add_responsible_button()

    def test_can_see_performer_creation(self, browser):
        self.page.should_be_add_responsible_button()
        self.page.go_to_add_responsible()
        self.page.should_be_responsible_creation()

    def test_cant_see_performer_creation(self, browser):
        self.page.should_be_add_responsible_button()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_responsible_creation(ResponsiblePage.NOT_PRESENT)

    def test_can_cancel_performer_creation(self, browser):
        self.page.go_to_add_responsible()
        self.page.close_drawer()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_responsible_creation(ResponsiblePage.DISAPPEAR)


@pytest.mark.responsible
@pytest.mark.responsible_creation
class TestResponsibleCreation:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, main_link)
        page.open()
        page.should_be_auth_page()
        login = os.getenv('DKRS_ADMIN_LOGIN')
        password = os.getenv('DKRS_ADMIN_PASSWORD')
        page.auth(login, password)

        self.page = ResponsiblePage(browser, main_link)

        self.page.should_be_add_responsible_button()
        self.fio = f'!000_AUTOTEST_11{2_000_000_000 - int(time.time())}'
        self.email = f'{2_000_000_000 - int(time.time())}@autotest.top'
        self.raw_phone = str(int(time.time()))[:10]
        self.phone = f'+7 {self.raw_phone[:3]} {self.raw_phone[3:6]} {self.raw_phone[6:8]} {self.raw_phone[8:]}'
        self.password = 'AUTOTEST IS THE BEST'
        self.object_n_services = [True, False, True, False, True]
        self.page.go_to_add_responsible()

        self.page.add_responsible(self.fio, self.email, self.raw_phone, self.password, self.object_n_services)
        time.sleep(1)
        yield
        try:
            self.page.go_to_archive()
            self.page.archive()
        except Exception as e:
            archive_fail(e, self.fio)

    def test_cant_see_performer_creation_after_creation(self, browser):
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_responsible_creation(ResponsiblePage.DISAPPEAR)

    def test_cant_see_performer_detailed_info_after_creation(self, browser):
        self.page.browser.implicitly_wait(0)
        time.sleep(3)
        self.page.should_not_be_responsible_detailed_info(ResponsiblePage.NOT_PRESENT)

    def test_expected_performer_info_equals_actual(self, browser):
        self.page.check_responsible_info(self.fio, self.email, self.phone, self.object_n_services)

    def test_can_see_and_close_performer_detailed_info(self, browser):
        self.page.go_to_detailed_info()
        self.page.should_be_responsible_detailed_info()
        self.page.close_drawer()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_responsible_detailed_info(ResponsiblePage.DISAPPEAR)

    def test_expected_performer_detailed_info_equals_actual(self, browser):
        self.page.go_to_detailed_info()
        self.page.check_responsible_detailed_info(self.fio, self.email, self.phone, self.object_n_services)
        self.page.close_drawer()

    def test_edit_and_save_see_summary(self, browser):
        fio, email, phone, object_n_services = f'!000_EDITED_{self.fio}', \
                                               f'{str(int(time.time()))[:10]}@edited_autotest.top', \
                                               str(int(time.time()))[:10], \
                                               [False, True, False, False, True]

        self.page.go_to_detailed_info()
        self.page.edit_responsible(fio=fio, email=email, phone=phone, object_n_services=object_n_services)
        self.page.save_responsible()

        expected_phone = f'+7 {phone[:3]} {phone[3:6]} {phone[6:8]} {phone[8:]}'
        self.page.check_responsible_info(fio, email, expected_phone, object_n_services)

    def test_edit_and_save_see_draft(self, browser):
        fio, email, phone, object_n_services = f'!000_EDITED_{self.fio}', \
                                               f'{str(int(time.time()))[:10]}@edited_autotest.top', \
                                               str(int(time.time()))[:10], \
                                               [False, True, False, False, True]

        self.page.go_to_detailed_info()
        self.page.edit_responsible(fio=fio, email=email, phone=phone, object_n_services=object_n_services)
        self.page.save_responsible()

        expected_phone = f'+7 {phone[:3]} {phone[3:6]} {phone[6:8]} {phone[8:]}'
        self.page.go_to_detailed_info()
        self.page.check_responsible_detailed_info(fio, email, expected_phone, object_n_services)
        self.page.close_drawer()

    def test_edit_and_not_save_see_summary(self, browser):
        fio, email, phone, object_n_services = f'!000_EDITED_{self.fio}', \
                                               f'{str(int(time.time()))[:10]}@edited_autotest.top', \
                                               str(int(time.time()))[:10], \
                                               [False, True, False, False, True]

        self.page.go_to_detailed_info()
        self.page.edit_responsible(fio=fio, email=email, phone=phone, object_n_services=object_n_services)
        self.page.close_drawer()  # просто закрываем, не сохраняем!

        # поэтому сверяем со старыми данными (дефолтными)
        self.page.check_responsible_info(self.fio, self.email, self.phone, self.object_n_services)

    @pytest.mark.fast
    def test_edit_and_not_save_see_draft(self, browser):
        fio, email, phone, object_n_services = f'!000_EDITED_{self.fio}', \
                                               f'{str(int(time.time()))[:10]}@edited_autotest.top', \
                                               str(int(time.time()))[:10], \
                                               [False, True, False, False, True]

        self.page.go_to_detailed_info()
        self.page.edit_responsible(fio=fio, email=email, phone=phone, object_n_services=object_n_services)
        self.page.close_drawer()  # просто закрываем, не сохраняем!

        # поэтому сверяем со старыми данными (дефолтными)
        self.page.go_to_detailed_info()
        self.page.check_responsible_detailed_info(self.fio, self.email, self.phone, self.object_n_services)
        self.page.close_drawer()

    def test_can_see_change_password_dialog(self, browser):
        self.page.go_to_detailed_info()
        self.page.go_to_change_password()
        self.page.should_be_responsible_change_password()

    def test_can_close_change_password_dialog(self, browser):
        self.page.go_to_detailed_info()
        self.page.go_to_change_password()
        self.page.close_dialog()
        self.page.should_not_be_responsible_change_password(ResponsiblePage.DISAPPEAR)

# АТЕНШОН! Тесты ниже не работают.


'''@pytest.mark.performer
@pytest.mark.performer_blacklist
class TestPerformerBlacklist:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, main_link)
        page.open()
        page.should_be_auth_page()
        login = os.getenv('DKRS_ADMIN_LOGIN')
        password = os.getenv('DKRS_ADMIN_PASSWORD')
        page.auth(login, password)

        self.page = PerformerPage(browser, main_link)

        self.page.should_be_add_performer_button()
        self.performer_fio = f'!000_AUTOTEST_11{2_000_000_000 - int(time.time())}'
        self.birthyear = '1996'
        self.raw_passport = '3697123456'
        self.passport = f'{self.raw_passport[:4]} {self.raw_passport[4:]}'
        self.raw_phone = str(int(time.time()))[:10]
        self.phone = f'+7 {self.raw_phone[:3]} {self.raw_phone[3:6]} {self.raw_phone[6:8]} {self.raw_phone[8:]}'
        self.inn = '8383838383838383838'
        self.bank_card = '5454545454545454'
        self.page.go_to_add_performer()

        self.page.add_performer(self.performer_fio, self.birthyear, self.passport, self.phone)
        time.sleep(1)
        yield
        try:
            if self.page.get_current_tab() == PerformerPage.ACTIVE_TAB:
                self.page.go_to_blacklist()
                self.page.blacklist()
        except Exception as e:
            blacklist_fail(e, self.performer_fio)

    def test_can_open_blacklist_tab(self, browser):
        self.page.go_to_removed_tab()

    def test_can_blacklist_person(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()

    def test_can_cancel_blacklist(self, browser):
        self.page.go_to_blacklist()
        self.page.cancel_blacklist()
        self.page.check_performer_info(self.performer_fio, self.phone)

    def test_check_blacklisted_person_info(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()
        self.page.go_to_removed_tab()
        self.page.check_performer_info(self.performer_fio, self.phone)

    def test_check_blacklisted_person_detailed_info(self, browser):
        comment = str(int(time.time()))
        self.page.go_to_blacklist()
        self.page.blacklist(str(int(time.time())))
        self.page.go_to_removed_tab()
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear, self.passport, self.phone,
                                                expected_status=PerformerPage.BLACKLIST_STATUS,
                                                expected_comment=comment)

    def test_check_blacklist_comment(self, browser):
        comment = 'This is a test comment made by auto-test!'

        self.page.go_to_blacklist()
        self.page.blacklist(comment)
        self.page.go_to_removed_tab()
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear, self.passport, self.phone,
                                                expected_status=PerformerPage.BLACKLIST_STATUS,
                                                expected_comment=comment)

    def test_can_blacklist_through_detailed_info_and_save(self, browser):
        comment = 'This is a test comment made by auto-test! Commented in detailed info!'

        self.page.go_to_detailed_info()
        self.page.change_performer_status(PerformerPage.BLACKLIST_STATUS, comment)
        self.page.save_performer()

        self.page.go_to_removed_tab()
        self.page.check_performer_info(self.performer_fio, self.phone)
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear, self.passport, self.phone,
                                                expected_status=PerformerPage.BLACKLIST_STATUS,
                                                expected_comment=comment)

    def test_can_blacklist_through_detailed_info_and_not_save(self, browser):
        comment = 'This is a test comment made by auto-test! Commented in detailed info!'

        self.page.go_to_detailed_info()
        self.page.change_performer_status(PerformerPage.BLACKLIST_STATUS, comment)
        self.page.close_drawer()  # просто закрываем, не сохраняем!

        # self.page.go_to_removed_tab()  # поэтому лицо должно остаться в списке активных
        self.page.check_performer_info(self.performer_fio, self.phone)
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear, self.passport, self.phone)
        self.page.close_drawer()

    def test_can_unblacklist_person(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()
        self.page.go_to_removed_tab()
        self.page.go_to_unblacklist()
        self.page.unblacklist()
        self.page.go_to_active_tab()
        self.page.check_performer_info(self.performer_fio, self.phone)
        self.page.close_drawer()

    def test_can_cancel_unblacklist_person(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()
        self.page.go_to_removed_tab()
        self.page.go_to_unblacklist()
        self.page.cancel_unblacklist()
        self.page.check_performer_info(self.performer_fio, self.phone)

    def test_can_unblacklist_through_detailed_info_and_save(self, browser):
        comment = 'This is a test comment made by auto-test! Commented in detailed info!'

        self.page.go_to_detailed_info()
        self.page.change_performer_status(PerformerPage.BLACKLIST_STATUS, comment)
        self.page.save_performer()

        self.page.go_to_removed_tab()
        self.page.go_to_detailed_info()
        self.page.change_performer_status(PerformerPage.ACTIVE_STATUS)
        self.page.save_performer()

        self.page.go_to_active_tab()
        self.page.check_performer_info(self.performer_fio, self.phone)
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear, self.passport, self.phone)

    def test_can_unblacklist_through_detailed_info_and_not_save(self, browser):
        comment = 'This is a test comment made by auto-test! Commented in detailed info!'

        self.page.go_to_detailed_info()
        self.page.change_performer_status(PerformerPage.BLACKLIST_STATUS, comment)
        self.page.save_performer()

        self.page.go_to_removed_tab()
        self.page.go_to_detailed_info()
        self.page.change_performer_status(PerformerPage.ACTIVE_STATUS)
        self.page.close_drawer()  # просто закрываем, не сохраняем!

        # self.page.go_to_active_tab()  # поэтому лицо должно остаться в чёрном списке
        self.page.check_performer_info(self.performer_fio, self.phone)
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear, self.passport, self.phone,
                                                expected_status=PerformerPage.BLACKLIST_STATUS,
                                                expected_comment=comment)
'''