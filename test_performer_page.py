import os
import time
import pytest
from pages.auth_page import AuthPage
from pages.order_page_READONLY import OrderPage  # TODO: удаляй при мне
from pages.performer_page import PerformerPage

main_link = 'https://test.dkrs.itmegastar.com/#/'


@pytest.fixture(scope='function', autouse=True)
def setup(browser):
    global page

    page = AuthPage(browser, main_link)
    page.open()
    page.should_be_auth_page()
    login = os.getenv('DKRS_ADMIN_LOGIN')
    password = os.getenv('DKRS_ADMIN_PASSWORD')
    page.auth(login, password)

    page = PerformerPage(browser, main_link)


@pytest.mark.performer
@pytest.mark.performer_basis
class TestPerformerBasis:

    def test_can_see_performer_add_button(self, browser):
        page.should_be_add_performer_button()

    def test_can_see_performer_creation(self, browser):
        page.should_be_add_performer_button()
        page.go_to_add_performer()
        page.should_be_performer_creation()

    def test_cant_see_performer_creation(self, browser):
        page.should_be_add_performer_button()
        page.browser.implicitly_wait(0)
        page.should_not_be_performer_creation(PerformerPage.NOT_PRESENT)

    def test_can_cancel_performer_creation(self, browser):
        page.go_to_add_performer()
        page.close_drawer()
        page.browser.implicitly_wait(0)
        page.should_not_be_performer_creation(PerformerPage.DISAPPEAR)


# @pytest.mark.order    # TODO: переписать маркеры
# @pytest.mark.order_creation
class TestOrderCreation:
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
        self.performer_fio = f'111_AUTOTEST_{int(time.time())}'
        self.birthyear = '1996'
        self.passport = '3697123456'
        self.phone = str(int(time.time()))[:10]
        self.inn = '8383838383838383838'
        self.bank_card = '5454545454545454'
        self.page.go_to_add_performer()

        self.page.add_performer(self.performer_fio, self.birthyear, self.passport, self.phone)
        time.sleep(1)
        yield
        try:
            self.page.go_to_blacklist()
            self.page.blacklist()
        except Exception as e:
            print('>> ERROR!: Failed deleting the performer.')
            print(f'>> Reason: {e}')
            print(f'>> Delete the performer with this FIO: {self.performer_fio}')

    def test_cant_see_performer_creation_after_creation(self, browser):
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_performer_creation(PerformerPage.DISAPPEAR)

    def test_cant_see_performer_detailed_info_after_creation(self, browser):
        self.page.browser.implicitly_wait(0)
        time.sleep(3)
        self.page.should_not_be_performer_detailed_info(PerformerPage.NOT_PRESENT)

    def test_expected_performer_info_equals_actual(self, browser):
        expected_phone = f'+7 {self.phone[:3]} {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}'
        self.page.check_performer_info(self.performer_fio, expected_phone)

    def test_can_see_performer_detailed_info(self, browser):
        self.page.go_to_detailed_info()
        self.page.should_be_performer_detailed_info()

    def test_can_close_performer_detailed_info(self, browser):
        self.page.go_to_detailed_info()
        self.page.should_be_performer_detailed_info()
        self.page.close_drawer()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_performer_detailed_info(PerformerPage.DISAPPEAR)

    def test_expected_performer_detailed_info_equals_actual(self, browser):
        self.page.go_to_detailed_info()
        expected_phone = f'+7 {self.phone[:3]} {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}'
        self.page.check_performer_detailed_info(self.performer_fio, self.birthyear,
                                                f'{self.passport[:4]} {self.passport[4:]}', expected_phone)
        self.page.close_drawer()

    def test_edit_and_save_see_summary(self, browser):
        fio, phone = f'111_EDITED_{self.performer_fio}', str(int(time.time()))[:10]

        self.page.go_to_detailed_info()
        self.page.edit_performer(fio=fio, phone=phone)
        self.page.save_performer()

        expected_phone = f'+7 {phone[:3]} {phone[3:6]} {phone[6:8]} {phone[8:]}'
        self.page.check_performer_info(expected_fio=fio, expected_phone=expected_phone)

    def test_edit_and_save_see_draft(self, browser):
        fio, birthyear = f'111_EDITED_{self.performer_fio}', '2002',
        passport, phone = "1111 222222", str(int(time.time()))[:10]

        self.page.go_to_detailed_info()
        self.page.edit_performer(fio=fio, birthyear=birthyear, passport=passport, phone=phone)
        self.page.save_performer()

        expected_phone = f'+7 {phone[:3]} {phone[3:6]} {phone[6:8]} {phone[8:]}'
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(expected_fio=fio, expected_birthyear=birthyear,
                                                expected_passport=passport, expected_phone=expected_phone)
        self.page.close_drawer()

    def test_edit_and_not_save_see_summary(self, browser):
        fio, phone = f'111_EDITED_{self.performer_fio}', str(int(time.time()))[:10]

        self.page.go_to_detailed_info()
        self.page.edit_performer(fio=fio, phone=phone)
        self.page.close_drawer()  # просто закрываем, не сохраняем!

        # поэтому сверяем со старыми данными (дефолтными)
        expected_phone = f'+7 {self.phone[:3]} {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}'
        self.page.check_performer_info(expected_fio=self.performer_fio, expected_phone=expected_phone)

    def test_edit_and_not_save_see_draft(self, browser):
        fio, birthyear = f'111_EDITED_{self.performer_fio}', '2002',
        passport, phone = "1111 222222", str(int(time.time()))[:10]

        self.page.go_to_detailed_info()
        self.page.edit_performer(fio=fio, birthyear=birthyear, passport=passport, phone=phone)
        self.page.close_drawer()  # просто закрываем, не сохраняем!

        # поэтому сверяем со старыми данными (дефолтными)
        expected_phone = f'+7 {self.phone[:3]} {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}'
        expected_passport = f'{self.passport[:4]} {self.passport[4:]}'
        self.page.go_to_detailed_info()
        self.page.check_performer_detailed_info(expected_fio=self.performer_fio, expected_birthyear=self.birthyear,
                                                expected_passport=expected_passport, expected_phone=expected_phone)
        self.page.close_drawer()

    def test_performer_should_be_selected_if_no_inn_and_no_bank_card(self, browser):
        self.page.check_performer_selection(True)
        self.page.go_to_blacklist()
        self.page.blacklist()

    def test_performer_should_be_selected_if_inn_and_no_bank_card(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()

        phone = str(int(time.time()))[:10]
        self.page.go_to_add_performer()
        self.page.add_performer(self.performer_fio, self.birthyear, self.passport, phone, inn=self.inn)

        self.page.check_performer_selection(True)

    def test_performer_should_be_selected_if_no_inn_and_bank_card(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()

        phone = str(int(time.time()))[:10]
        self.page.go_to_add_performer()
        self.page.add_performer(self.performer_fio, self.birthyear, self.passport, phone, bank_card=self.bank_card)

        self.page.check_performer_selection(True)

    @pytest.mark.fast
    def test_performer_should_not_be_selected_if_inn_and_bank_card(self, browser):
        self.page.go_to_blacklist()
        self.page.blacklist()

        phone = str(int(time.time()) + 2)[:10]
        self.page.go_to_add_performer()
        self.page.add_performer(self.performer_fio, self.birthyear, self.passport, phone, inn=self.inn,
                                bank_card=self.bank_card)

        self.page.check_performer_selection(False)


# @pytest.mark.order_element
# @pytest.mark.order_element_basis
class TestOrderElementBasis:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, main_link)
        page.open()
        page.should_be_auth_page()
        email = os.getenv('SPRING_ADMIN_MAIL')
        password = os.getenv('SPRING_ADMIN_PASSWORD')
        page.auth(email, password)

        self.page = OrderPage(browser, main_link)

        self.page.should_be_create_order_button()
        self.order_number = f'AUTOTEST_{int(time.time())}'
        self.page.go_to_create_order()
        time.sleep(.5)
        self.page.create_order(self.order_number)
        time.sleep(1)

    def test_can_add_element(self, browser):
        self.page.should_be_order_draft()

    def test_can_see_element_creation(self, browser):
        self.page.should_be_order_draft()
        self.page.go_to_create_element()
        self.page.should_be_element_creation()

    def test_cant_see_element_creation(self, browser):
        self.page.should_be_order_draft()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('pres')

    def test_can_cancel_element_creation(self, browser):
        self.page.go_to_create_element()
        self.page.go_to_cancel_element()
        self.page.cancel('leave')
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('dis')

    def test_can_go_back_to_element_creation(self, browser):
        self.page.go_to_create_element()
        self.page.go_to_cancel_element()
        self.page.cancel('cancel')
        self.page.should_be_element_creation()


# @pytest.mark.order_element
# @pytest.mark.order_element_creation
class TestOrderElementCreation:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, main_link)
        page.open()
        page.should_be_auth_page()
        email = os.getenv('SPRING_ADMIN_MAIL')
        password = os.getenv('SPRING_ADMIN_PASSWORD')
        page.auth(email, password)

        self.page = OrderPage(browser, main_link)

        self.page.should_be_create_order_button()
        self.order_number = f'AUTOTEST_{int(time.time())}'
        self.page.go_to_create_order()
        self.page.create_order(self.order_number)
        self.page.should_be_order_draft()
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(1)

    def test_can_see_order_draft_after_creation(self, browser):
        self.page.should_be_order_draft()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('dis')

    def test_expected_element_info_equals_actual(self, browser):
        time.sleep(2)
        self.page.check_element_info()

    def test_save_and_reload(self, browser):
        self.page.save_order()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_be_any_element()

    def test_save_then_check(self, browser):
        self.page.save_order()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        time.sleep(2)
        self.page.check_element_info()

    def test_not_save_and_reload(self, browser):
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_any_element()  # поэтому элементов не должно быть

    def test_delete_save_and_reload(self, browser):
        self.page.save_order()
        self.page.go_to_delete_element()
        self.page.delete_element('delete')
        self.page.save_order()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_not_be_any_element()

    def test_delete_not_save_and_reload(self, browser):
        self.page.save_order()
        self.page.go_to_delete_element()
        self.page.delete_element('delete')
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_be_any_element()  # поэтому элемент должен остаться

    def test_can_cancel_deletion(self, browser):
        self.page.go_to_delete_element()
        self.page.delete_element('cancel')
        self.page.should_be_any_element()

    def test_can_add_few_elements(self, browser):
        # time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        # time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)

    def test_can_add_few_elements_and_save(self, browser):
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)
        self.page.save_order()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.count_elements(3)

    def test_can_add_few_elements_and_not_save(self, browser):
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_not_be_any_element()  # поэтому элементов не должно быть

    def test_can_add_few_elements_and_save_then_add_few_elements_and_save(self, browser):
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)
        self.page.save_order()
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(6)
        self.page.save_order()
        time.sleep(1)
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.count_elements(6)

    def test_can_add_few_elements_and_save_then_add_few_elements_and_not_save(self, browser):
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.count_elements(3)
        self.page.save_order()
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.count_elements(6)
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.count_elements(3)  # поэтому элементов должно быть 3

    def test_can_edit_element(self):
        self.page.should_be_order_draft()
        self.page.should_be_any_element()

    def test_can_see_element_edit(self, browser):
        self.page.should_be_order_draft()
        self.page.should_be_any_element()
        self.page.go_to_edit_element()
        self.page.should_be_element_creation()

    def test_cant_see_element_edit(self, browser):
        self.page.should_be_order_draft()
        self.page.should_be_any_element()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('pres')

    def test_can_cancel_element_edit(self, browser):
        self.page.go_to_edit_element()
        self.page.go_to_cancel_element()
        self.page.cancel('leave')
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('dis')

    def test_can_go_back_to_element_edit(self, browser):
        self.page.go_to_edit_element()
        self.page.go_to_cancel_element()
        self.page.cancel('cancel')
        self.page.should_be_element_creation()

    def test_edit_element(self, browser):
        sett = ('F', 'Motoröl für FIAT 2015 Release der C-Serie'
                     ' in der maximalen Konfiguration (0004)', 4, 'testacc (0003)',
                     'MVZ 3 (0002)', 'Вн заказ 1 (0001)', 34.61, 'Склад 1', 'Ряд 1',
                     'Стеллаж 1', 'Полка 1', 'Ячейка 1')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)

    def test_expected_edited_element_equals_actual(self, browser):
        sett = ('F', 'Motoröl für FIAT 2015 Release der C-Serie'
                     ' in der maximalen Konfiguration (0004)', 4, 'testacc (0003)',
                     'MVZ 3 (0002)', 'Вн заказ 1 (0001)', 34.61, 'Склад 1', 'Ряд 1',
                     'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        sett = ('F', 'testacc', 'MVZ 3', 'Вн заказ 1',
                'Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration',
                '4', '138,44', '34,61', 'Stuck')

        self.page.check_element_info(*sett)

    def test_edit_element_then_save_and_check(self, browser):
        sett = ('F', 'Motoröl für FIAT 2015 Release der C-Serie'
                     ' in der maximalen Konfiguration (0004)', 4, 'testacc (0003)',
                'MVZ 3 (0002)', 'Вн заказ 1 (0001)', 34.61, 'Склад 1', 'Ряд 1',
                'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        self.page.save_order()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        sett = ('F', 'testacc', 'MVZ 3', 'Вн заказ 1',
                'Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration',
                '4', '138,44', '34,61', 'Stuck')

        self.page.check_element_info(*sett)

    def test_edit_element_then_not_save_and_check(self, browser):
        sett = ('F', 'Motoröl für FIAT 2015 Release der C-Serie'
                     ' in der maximalen Konfiguration (0004)', 4, 'testacc (0003)',
                'MVZ 3 (0002)', 'Вн заказ 1 (0001)', 34.61, 'Склад 1', 'Ряд 1',
                'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.check_element_info()  # поэтому сверяем со старыми данными (дефолтными)

    def test_edit_element_then_save_then_edit_element_then_save_and_check(self, browser):
        sett = ('F', 'Motoröl für FIAT 2015 Release der C-Serie'
                     ' in der maximalen Konfiguration (0004)',
                4, 'testacc (0003)', 'MVZ 3 (0002)', 'Вн заказ 1 (0001)', 34.61, 'Склад 1', 'Ряд 1',
                'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        sett = ('K', 'Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65, NBR (blau),'
                     ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                3, 'Regress sachkonto (003)', 'Double Regress MVZ (001)', 'Double regress inner order (001)',
                16.00, 'Lager of Magazine №2', 'Reihe 1', 'Stack 1', 'Board 1', 'Cell 1', 'Подяейка 1')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        self.page.save_order()
        self.page.check_element_info()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.check_element_info()

    def test_edit_element_then_save_then_edit_element_then_not_save_and_check(self, browser):
        sett = ('F', 'Motoröl für FIAT 2015 Release der C-Serie'
                     ' in der maximalen Konfiguration (0004)',
                4, 'testacc (0003)', 'MVZ 3 (0002)', 'Вн заказ 1 (0001)', 34.61, 'Склад 1', 'Ряд 1',
                'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        sett = ('K', 'Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65, NBR (blau),'
                     ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                3, 'Regress sachkonto (003)', 'Double Regress MVZ (001)', 'Double regress inner order (001)',
                16.00, 'Lager of Magazine №2', 'Reihe 1', 'Stack 1', 'Board 1', 'Cell 1', 'Подяейка 1')
        self.page.save_order()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        # self.page.save_order()  # не сохраняем!
        self.page.check_element_info()
        OrderPage(browser, main_link).open()
        time.sleep(1)
        self.page.go_to_work()
        sett = ('F', 'testacc', 'MVZ 3', 'Вн заказ 1',
                'Motoröl für FIAT 2015 Release der C-Serie'
                ' in der maximalen Konfiguration',
                '4', '138,44', '34,61', 'Stuck')

        self.page.check_element_info(*sett)
